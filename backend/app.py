import base64
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

@app.route('/api/results', methods=['GET'])
def query():
    return

@app.route('/api/image', methods=['GET'])
def image():
    if request.method == "POST":
        img = request.json
        image = base64.b64decode(img['image'])
        with open(r'test.jpg', 'wb') as f: # change file name
            f.write(image)
            
    return "Completed! Image is now loaded as test.jpg!" # change name 

if __name__ == '__main__':
    app.run(debug=True)