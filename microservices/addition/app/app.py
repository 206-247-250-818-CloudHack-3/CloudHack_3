from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class addition(Resource):
    def get(self, a, b):
        x = int(a) + int(b)
        return x
    
api.add_resource(addition, '/<string:a>/<string:b>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5051,
        host="0.0.0.0"
    )
