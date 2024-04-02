from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(string)  # Print the string in the console
    return f'<h2>{string}</h2>'  # Display the string in the web browser

@app.route('/count/<int:num>')
def count(num):
    numbers = '<br>'.join(str(i) for i in range(1, num+1))
    return f'<h2>{numbers}</h2>'

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<h2>Error: Division by zero</h2>'
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return '<h2>Error: Modulo by zero</h2>'
    else:
        return '<h2>Error: Invalid operation</h2>'
    
    return f'<h2>Result: {result}</h2>'

if __name__ == '__main__':
    app.run(debug=True)
