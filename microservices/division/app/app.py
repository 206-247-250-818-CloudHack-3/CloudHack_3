from flask import Flask
from flask_restful import Api, Resource
import requests
import os

app = Flask(__name__)
api = Api(app)

# Create a class which inherits Resource class from flask_restful
class Division(Resource):
    def get(self, n1, n2):
        m = float(n1)
        n = float(n2)
        x = float(m/n)   
        return x

api.add_resource(Division, '/<int:n1>/<int:n2>')
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5054,
        host="0.0.0.0"
    )