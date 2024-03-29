from flask import Flask
from flask_restful import Api, Resource
import requests
import os

app = Flask(__name__)
api = Api(app)

# Create a class which inherits Resource class from flask_restful
class Sub(Resource):
    def get(self, n1, n2):
        return int(n1) - int(n2)


api.add_resource(Sub, '/<string:n1>/<string:n2>')
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5052,
        host="0.0.0.0"
    )
