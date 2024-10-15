from flask_restful import Resource
from flask import jsonify, request, make_response
from datetime import datetime
from flask_security import roles_accepted, current_user

from models import Category, db

class CategoryResource(Resource):
    from flask_security import auth_token_required
    @auth_token_required
    @roles_accepted('admin', 'manager')
    def post(self):
        data = request.get_json()
        name = data['name']
        if not name:
            return make_response(jsonify({"message": "name is required"}), 404)
        description = data['description']
        if not description:
            return make_response(jsonify({"message": "description is required"}), 404)
        if current_user.has_role('admin'):
            cate = Category(name=name, description=description, status=True, created_at=datetime.now(), created_by=current_user.id)
        else:
            cate = Category(name=name, description=description, status=False, created_at=datetime.now(), created_by=current_user.id)
        db.session.add(cate)
        db.session.commit()
        # cache.clear()
        return make_response(jsonify({"message": "category created successfully", "id": cate.id, "name": cate.name, "status": cate.status}), 201)

    @roles_accepted('admin', 'manager', 'customer')
    def get(self):
        categories = Category.query.all()
        data = [category.serialize() for category in categories]
        '''
        data = []
        for categories in category:
            cate = {
                    'id': categories.id,
                    'name': categories.name,
                    'description': categories.description,
                    'status': categories.status,
                    'created_at': categories.created_at,
                    'created_by': categories.created_by,
                    'updated_at': categories.updated_at,
                    'updated_by': categories.updated_by
                }
            data.append(cate)
        '''
        # print(data)
        if not data:
            return make_response(jsonify({"message": "No category found"}), 404)
        return make_response(jsonify({"message": "get all categories", "data": data}), 200)
    
class CategorySpecific(Resource):
    @roles_accepted('admin', 'manager', 'customer')
    def get(self, id):
        categories = Category.query.filter_by(id=id).first()
        cate = categories.serialize()
        if not cate:
            return make_response(jsonify({"message": "No category found by that id"}), 404)
        return jsonify({"message": "category Present", "data": cate})
    
    @roles_accepted('admin', 'manager')
    def put(self, id):
        categories = Category.query.filter_by(id=id).first()
        if not categories:
            return make_response(jsonify({"message": "No category found by that id"}), 404)
        data = request.get_json()
        name = data['name']
        if not name:
            return jsonify({"message": "name is required"})
        description = data['description']
        if not description:
            return jsonify({"message": "description is required"})
        categories.name = name
        categories.description = description
        categories.updated_at = datetime.now()
        categories.updated_by = current_user.id
        if current_user.has_role('admin'):
            categories.status = True
        else:
            categories.status = False
        db.session.commit()
        return make_response(jsonify({"message": "update specific category", 'id': id}), 201)
    
    @roles_accepted('admin', 'manager')
    def delete(self, id):
        categories = Category.query.filter_by(id=id).first()
        if not categories:
            return make_response(jsonify({"message": "No category found by that id"}), 404)
        categories.delete = True
        db.session.commit()
        return make_response(jsonify({"message": "delete specific category", 'id': id}), 201)
    

class newCategorySpecific(Resource):
    @roles_accepted('admin', 'manager', 'customer')
    def get(self):
        id = request.json.get('id')
        categories = Category.query.filter_by(id=id).first()
        cate = categories.serialize()
        if not cate:
            return make_response(jsonify({"message": "No category found by that id"}), 404)
        return jsonify({"message": "category Present", "data": cate})
    
    @roles_accepted('admin', 'manager')
    def put(self):
        id = request.json.get('id')
        categories = Category.query.filter_by(id=id).first()
        if not categories:
            return make_response(jsonify({"message": "No category found by that id"}), 404)
        data = request.get_json()
        name = data['name']
        if not name:
            return jsonify({"message": "name is required"})
        description = data['description']
        if not description:
            return jsonify({"message": "description is required"})
        categories.name = name
        categories.description = description
        categories.updated_at = datetime.now()
        categories.updated_by = current_user.id
        if current_user.has_role('admin'):
            categories.status = True
        else:
            categories.status = False
        db.session.commit()
        return make_response(jsonify({"message": "update specific category", 'id': id}), 201)
    
    @roles_accepted('admin', 'manager')
    def delete(self):
        id = request.json.get('id')
        categories = Category.query.filter_by(id=id).first()
        if not categories:
            return make_response(jsonify({"message": "No category found by that id"}), 404)
        categories.delete = True
        db.session.commit()
        return make_response(jsonify({"message": "delete specific category", 'id': id}), 201)