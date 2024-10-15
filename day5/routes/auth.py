from flask import request, jsonify, make_response
from flask_restful import Resource

from models import user_datastore, db

# @app.route('/signup', methods=['POST'])
# def signup():
class signup(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        if not email:
            return {"status": "please provide a email"}, 400
        password = data.get('password')
        if not password:
            return {"status": "please provide a password"}, 400
        
        role = data.get('role')
        if not role:
            return {"status": "please provide a role"}, 400
        if "admin" in role:
            return {"status": "admin cannot be created"}, 400

        # from models import User
        # new_user = User(email=email, password=password)
        # db.session.add(new_user)
        if user_datastore.find_user(email=email):
            return {"status": "email already used"}, 400
        # user_datastore.create_user(email=email, password=password, roles=[role])
        user = user_datastore.create_user(email=email, password=password)
        if "manager" in role:
            user_datastore.deactivate_user(user)
        for role in role:
            user_datastore.add_role_to_user(user, role)
        '''
        user_datastore.add_role_to_user(user, role)

        '''
        db.session.commit()

        return {"status": "success"}, 201


# @app.route('/signin', methods=['POST'])
# def signin():
class signin(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        if not email:
            return {"status": "please provide a email"}, 400
        password = data.get('password')
        if not password:
            return {"status": "please provide a password"}, 400
        user = user_datastore.find_user(email=email)
        if user and user.password == password:
            token = user.get_auth_token()
            return make_response(jsonify({"status": "success in loggin", "authToken": token}), 200)