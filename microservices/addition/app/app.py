from flask import Flask
from flask_restful import Api, Resource
import requests
import os

app = Flask(__name__)
api = Api(app)

class addition(Resource):
    def get(self, a, b):
        return a + b
    
api.add_resource(addition, '/<int:a>/<int:b>')

# Test the app
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5051,
        host="0.0.0.0"
    )
