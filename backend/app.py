from flask import Flask, request
from flask_cors import CORS
from mongo import addPerson

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.json['name']
        email = request.json['email']
        addPerson(name, email)
        print(request.json['name'])
        print(request.json['email'])
    return "Hello"

if __name__=='__main__':
   app.run(debug=True)