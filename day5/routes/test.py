from flask_restful import Resource
from flask import request, jsonify, make_response

class testapi(Resource):
    def get(self):
        return {"status": "success"}, 200

    def post(self):
        data = request.json
        return make_response(jsonify({"message": "post working", "testdata": data, "var4": [1,2,3,4], "var1": 1}), 201)
    
    def put(self):
        data = request.json
        return data, 200
    
    def delete(self):
        return {"status": "success"}, 200