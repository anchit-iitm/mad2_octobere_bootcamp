from flask import Flask, render_template, request, redirect, url_for # pip install flask

from flask_security import Security, auth_required, roles_accepted, roles_required # pip install flask-security

from models import mad1_ver, db, user_datastore

def create_celery(init_app):
    from celery import Celery
    init_celery = Celery(init_app.import_name)
    import celery_config
    init_celery.config_from_object(celery_config)
    return init_celery

def create_app():
    init_app = Flask(__name__)

    # import config
    # app.config.from_object(config)

    from config import localdev
    init_app.config.from_object(localdev)

    # db = SQLAlchemy(app)
    db.init_app(init_app)
    security=Security(init_app, user_datastore)

    from flask_restful import Api
    init_api = Api(init_app)

    from flask_cors import CORS
    CORS(init_app)

    return init_app, init_api
    # return init_app, init_api, init_celery

# app, api = create_app()
app, api = create_app()
# app_celery = create_celery(app)

from celery import Celery
app_celery = Celery(app.import_name)
import celery_config
app_celery.config_from_object('celery_config')
import celery_tasks
# from celery import Tas

@app.route('/helloworld')
def hello_world():
    return 'Hello, World! from anchit'

@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/testcelery', methods=['POST'])
def testcelery():
    data = request.json
    a,b = data['a'], data['b']
    print(type(a))
    # add.delay(a, b)
    result = celery_tasks.add.delay(a, b)
    while not result.ready():
        pass
    return {"status": result.status, "result": result.result, "id": result.id}, 201


@app.route('/test12345')
def test1():
    msg = 'hi campers'
    var2 = True
    var4 = ['iitm', 'iitkgp', 'iitb', 'iitd']
    return render_template('index1.html', var1=msg, var3=var2, var5=var4)

@app.route('/test2', methods=['GET', 'POST'])
def test2():
    if request.method == "POST":
        name_var = request.form.get('name')
        print(name_var)
        return render_template('index2.html')
    # if request.method == "GET":
    #     return render_template('index2.html')
    return render_template('index2.html')

@app.route('/test3', methods=['POST'])
def test3():
    name_var = request.form.get('name')
    print(name_var)
    # return redirect('/test1')
    return redirect(url_for('test1'))

@app.route('/test4', methods=['GET', 'POST'])
def test4():
    if request.method == "POST":
        name_var = request.form.get('name')
        # print(name_var)
        new_name = mad1_ver(name=name_var)
        db.session.add(new_name)
        db.session.commit()
        return render_template('index3.html')
    # if request.method == "GET":
    #     return render_template('index2.html')
    return render_template('index3.html')

@app.route('/test11')
@auth_required('token')
@roles_required('customer', 'manager')
# @roles_accepted('customer', 'manager')
def test11():
    msg = 'hi campers'
    var2 = True
    var4 = ['iitm', 'iitkgp', 'iitb', 'iitd']
    from models import User
    test = User.query.filter_by(id=1).first()
    # return render_template('index1.html', var1=msg, var3=var2, var5=var4)
    return {"var1": msg, "var3": var2, "var5": var4, "var6": "iitkgp"}

@app.route('/test14', methods=['POST'])
def test14():
    name_var = request.json.get('name')
    # print(name_var)
    if not name_var:
        return {"status": "failure"}, 400
    new_name = mad1_ver(name=name_var)
    db.session.add(new_name)
    db.session.commit()
    return {"status": "success"}, 201

@app.route('/test15', methods=['PUT'])
@auth_required('token')
@roles_required('manager')
def test15():
    name_var = request.json.get('name')
    name_var1 = request.json.get('updatedname')
    # print(name_var)
    if not name_var:
        return {"status": "failure"}, 400
    from models import mad1_ver
    name_entry = mad1_ver.query.filter_by(name=name_var).first()
    name_entry.name = name_var1
    db.session.commit()
    return {"status": "successfully updated"}, 201

@app.route('/test16', methods=['delete'])
@auth_required('token')
@roles_required('manager')
def test16():
    name_var = request.json.get('name')
    # print(name_var)
    if not name_var:
        return {"status": "failure"}, 400
    from models import mad1_ver
    name_entry = mad1_ver.query.filter_by(name=name_var).first()
    db.session.delete(name_entry)
    db.session.commit()
    return {"status": "successfully deleted"}, 201

from routes.auth import signup, signin
api.add_resource(signup, '/signup')
api.add_resource(signin, '/signin')

from routes.test import testapi
api.add_resource(testapi, '/testapi')

from routes.category import CategoryResource, CategorySpecific, newCategorySpecific
api.add_resource(CategoryResource, '/api/category')
api.add_resource(CategorySpecific, '/api/category/<int:id>') # accepts the id with the url
api.add_resource(newCategorySpecific, '/api/new/category') # accepts the id with the json body

from routes.product import ProductResource, ProductSpecific # type: ignore
api.add_resource(ProductResource, '/api/product')
api.add_resource(ProductSpecific, '/api/product/<int:id>')

from routes.admin import CategoryDelete, ProductDelete, toggle_user_status, UserResources # type: ignore
api.add_resource(CategoryDelete, '/api/category_delete/<int:id>')
api.add_resource(ProductDelete, '/api/product_delete/<int:id>')
api.add_resource(toggle_user_status, '/api/toggle_user_status/<int:id>')
api.add_resource(UserResources, '/api/users', '/api/user/<int:id>')



if __name__ == '__main__':
    app.run()