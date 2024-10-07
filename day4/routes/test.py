from flask_restful import Resource
from flask import request, jsonify, make_response

class testapi(Resource):
    def get(self):
        return {"status": "success"}, 200

    def post(self):
        data = request.json
        return data, 200
    
    def put(self):
        data = request.json
        return data, 200
    
    def delete(self):
        return {"status": "success"}, 200