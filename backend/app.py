from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/', methods=['POST', 'GET','OPTIONS'])
@cross_origin(supports_credentials=True)
def index():
    if request.method == 'POST':
        print(request.json['firstName'])
        print(request.json['lastName'])
        # name = request.json['name']
        # email = request.json['email']
        # addPerson(name, email)
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)
