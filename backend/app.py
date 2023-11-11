from flask import Flask, request
from flask_cors import CORS
from mongo import addPerson

app = Flask(__name__)
CORS(app)
CORS(app=True)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.json['name'])
        print(request.json['email'])
        name = request.json['name']
        email = request.json['email']
        addPerson(name, email)
    return "Hello"

if __name__=='__main__':
   app.run(debug=True)