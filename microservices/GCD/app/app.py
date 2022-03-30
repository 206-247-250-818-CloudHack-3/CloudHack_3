from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def calculate_gcd(a, b):

    if (a == 0):
        return b
    if (b == 0):
        return a
  
    # base case
    if (a == b):
        return a
  
    # a is greater
    if (a > b):
        return calculate_gcd(a-b, b)
        
    return calculate_gcd(a, b-a)

class gcd(Resource):
    def get(self, n1, n2):
        x = calculate_gcd(int(n1), int(n2))
        return x

api.add_resource(gcd, '/<string:n1>/<string:n2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5055,
        host="0.0.0.0"
    )