from flask_restful import Resource
from flask import jsonify, request, make_response
from datetime import datetime
from flask_security import roles_accepted, current_user

from models import Category, db, Product, user_datastore, User

class CategoryDelete(Resource):
    @roles_accepted('admin')
    def delete(self, id):
        status = Category.admin_delete(id)
        if status:
            return make_response(jsonify({"message": "category deleted successfully"}), 201)
        return make_response(jsonify({"message": "No category found by that id"}), 404)
    
class ProductDelete(Resource):
    @roles_accepted('admin')
    def delete(self, id):
        # print(id)
        status = Product.admin_delete(id)
        # status = True
        if status:
            return make_response(jsonify({"message": "product deleted successfully"}), 201)
        return make_response(jsonify({"message": "No product found by that id"}), 404)
    
class toggle_user_status(Resource):
    @roles_accepted('admin')
    def put(self, id):
        user = user_datastore.find_user(id=id)
        if not user:
            return make_response(jsonify({"message": "No user found by that id"}), 404)
        user_datastore.toggle_active(user)
        db.session.commit()
        return make_response(jsonify({"message": "user status updated successfully", "email": user.email, "status": user.active}), 201)
    
class UserResources(Resource):
    @roles_accepted('admin')
    def get(self):
        users = User.get_all_users()
        data = [user.serialize() for user in users]
        if not data:
            return make_response(jsonify({"message": "No user found"}), 404)
        return make_response(jsonify({"message": "get all users", "data": data}), 200)
    
    @roles_accepted('admin')
    def delete(self, id):
        user = user_datastore.find_user(id=id)
        if not user:
            return make_response(jsonify({"message": "No user found by that id"}), 404)
        user_datastore.delete_user(user)
        db.session.commit()
        return make_response(jsonify({"message": "user deleted successfully", "email": user.email}), 200)