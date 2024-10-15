from flask_restful import Resource
from flask import jsonify, request, make_response
from datetime import datetime
from flask_security import roles_accepted, current_user

from models import db, Product, Category

class ProductResource(Resource):
    @roles_accepted('admin', 'manager')
    def post(self):
        data = request.get_json()
        name = data['name']
        if not name:
            return make_response(jsonify({"message": "name is required"}), 404)
        description = data['description']
        if not description:
            return make_response(jsonify({"message": "description is required"}), 404)
        price = data['price']
        if not price:
            return make_response(jsonify({"message": "price is required"}), 404)
        stock = data['stock']
        if not stock:
            return make_response(jsonify({"message": "stock is required"}), 404)
        category_id = data['category_id']
        check = Category.query.filter_by(id=category_id).first()
        print(check)
        if not category_id:
            return make_response(jsonify({"message": "category_id is required"}), 404)
        
        if check:
            # if current_user.has_role('admin'):
            product = Product(name=name, description=description, price=price, stock=stock, category_id=category_id, created_by=current_user.id)
            db.session.add(product)
            db.session.commit()
            return make_response(jsonify({"message": "category created successfully", "id": product.id, "name": product.name}), 201)
        return make_response(jsonify({"message": "category_id is not present"}), 404)
        

    @roles_accepted('admin', 'manager', 'customer')
    def get(self):
        products = Product.query.all()
        data = [product.serialize() for product in products]
        # print(data)
        if not data:
            return make_response(jsonify({"message": "No product found"}), 404)
        return make_response(jsonify({"message": "get all products", "data": data}), 200)
    
class ProductSpecific(Resource):
    @roles_accepted('admin', 'manager', 'customer')
    def get(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            return make_response(jsonify({"message": "No product found by that id"}), 404)
        prod = product.serialize()
        return jsonify({"message": "get specific product", "data": prod})
    
    @roles_accepted('admin', 'manager')
    def put(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            return make_response(jsonify({"message": "No product found by that id"}), 404)
        data = request.get_json()
        name = data.get('name')
        if not name:
            return jsonify({"message": "name is required"})
        description = data.get('description')
        if not description:
            return jsonify({"message": "description is required"})
        price = data.get('price')
        if price is None:  # Assuming price can be 0, which is falsy
            return jsonify({"message": "price is required"})
        product.name = name
        product.description = description
        product.price = price
        product.updated_at = datetime.now()
        product.updated_by = current_user.id
        # if current_user.has_role('admin'):
        #     product.status = True
        # else:
        #     product.status = False
        db.session.commit()
        return jsonify({"message": "update specific product", 'id': id})
    
    @roles_accepted('admin', 'manager')
    def delete(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            return make_response(jsonify({"message": "No product found by that id"}), 404)
        product.delete = True  # Assuming there's a 'delete' attribute; might need adjustment
        db.session.commit()
        return make_response(jsonify({"message": "delete specific product", 'id': id}), 201)
    
    @roles_accepted('admin', 'manager')
    def patch(self, id):
        product = Product.query.filter_by(id=id).first()
        if not product:
            return make_response(jsonify({"message": "No product found by that id"}), 404)
        product.status = not product.status
        product.updated_by = current_user.id
        db.session.commit()
        if product.status:
            return jsonify({"message": "product activated", 'id': id})
        return jsonify({"message": "product deactivated", 'id': id})