from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello world'

hello_list = ["Hello", "World!"]
hello_dict = {"Hello": "World!"}

@app.route("/")
def home():
    return "Hi"

@app.route("/normal")
def normal():
    return str(hello_list)

@app.route("/jsonified")
def jsonified_list():
    return jsonify(hello_list)

@app.route("/dict")
def dictionary():
    return hello_dict