from flask import Flask, request
from flask_cors import CORS
from mongo import addPerson

app = Flask(__name__)
@app.route('/api/form', methods=['POST'])
def form():
    if request.method == 'POST':
        print(request.json['name'])
        print(request.json['email'])
        name = request.json['name']
        email = request.json['email']
        spire = request.json['spire']
        addPerson(name, email, spire)
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)