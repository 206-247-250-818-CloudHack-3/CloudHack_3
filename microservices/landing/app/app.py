from flask import Flask, render_template, request, flash, redirect
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

def add(n1, n2):
    return int(requests.get('http://addition:5051/'+str(n1)+'/'+str(n2)).text)

def minus(n1, n2):
    return int(requests.get('http://subtraction:5052/'+str(n1)+'/'+str(n2)).text)

def multiply(n1, n2):
    return int(requests.get('http://multiplication:5053/'+str(n1)+'/'+str(n2)).text)

def divide(n1, n2):
    return int(requests.get('http://division:5054/'+str(n1)+'/'+str(n2)).text)

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get('first', type=int)
    number_2 = request.form.get('second', type=int)
    operation = request.form.get('operation')
    result = 0
    try:
        if operation == 'add':
            result = add(number_1, number_2)
        elif operation == 'minus':
            result =  minus(number_1, number_2)
        elif operation == 'multiply':
            result = multiply(number_1, number_2)
        elif operation == 'divide':
            result = divide(number_1, number_2)

        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
    
    except:
        flash(f'Please enter two input numbers')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
