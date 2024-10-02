from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'

db = SQLAlchemy(app)

class mad1_ver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

with app.app_context():
    db.create_all()

@app.route('/helloworld')
def hello_world():
    return 'Hello, World! from anchit'

@app.route('/test')
def test():
    return render_template('index.html')


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
def test11():
    msg = 'hi campers'
    var2 = True
    var4 = ['iitm', 'iitkgp', 'iitb', 'iitd']
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

if __name__ == '__main__':
    app.run()