from flask import Flask
from flask_restful import Api, Resource
import math

app = Flask(__name__)
api = Api(app)

class exponent(Resource):
    def get(self, a, b):
        x = int(a) ** int(b)
        return x
    
api.add_resource(exponent, '/<string:a>/<string:b>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5057,
        host="0.0.0.0"
    )
