from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
   return "<h1>Hello world</h1>"

@app.route('/bonisam')
def hello():
    response = make_response("Hello world")
    response.status_code = 202
    response.headers['content-type'] = 'application/octet-stream'
    return response
    # if request.method == 'GET':
    #     return "You made a GET request"
    # elif request.method == 'POST':
    #     return "You made a POST request"
    # else:
    #     return "You will never see this message"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f"{number1} + {number2} = {number1 + number2}"


@app.route('/handle_url_params')
def handle_param():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f"{greeting}, {name}"
    else:
        return 'Some parameters are missing'




if __name__ == "__main__":
    app.run(debug=True)