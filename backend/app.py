import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
from mongo import addPerson
from pymongo.mongo_client import MongoClient
from bson import binary

app = Flask(__name__)

client = MongoClient("mongodb+srv://mkandeshwara:1234@printscanner.mgav5zb.mongodb.net/?retryWrites=true&w=majority")
db = client["people"]
user_collection = db["students"]
images = {}


@app.route('/api/form', methods=['POST'])
def form():
    # if request.method == 'POST':
    #     print(request.json['name'])
    #     print(request.json['email'])
    #     name = request.json['name']
    #     email = request.json['email']
    #     spire = request.json['spire']

  

    image_id = request.form.get('image_id', 'default')
    if image_id in images:
        image_binary = binary.Binary(images[image_id])

        name = request.form['name']
        email = request.form['email']
        spire = request.form['spire']

        user_document = {
        '_id' : spire,   
        'name' : name,
        'email' : email,
        'image' : image_binary
        }

        try:
            user_collection.insert_one(user_document)
            del images[image_id]
            return jsonify({"message":"Success"})
        except Exception as e:
            return jsonify({"message":str(e)}), 500
    else:
        return jsonify({"message":"Image not found"})
    

@app.route('/api/results', methods=['GET'])
def query():
    return

@app.route('/api/image', methods=['GET', 'POST'])
def image():
    #if request.method == "POST":
        #img = request.json
        #imageStr = base64.b64decode(img['image'])
        # with open(r'test.jpg', 'wb') as f: # change file name
        #     f.write(image)
            
    # return "Completed! Image is now loaded as test.jpg!" # change name
    img_data = request.json.get('image')

    if img_data is not None:
        image_id = request.json.get('id', 'default')
        images[image_id] = base64.b64encode(img_data)
        return jsonify({"message":"Image received", "id": image_id})
    return jsonify({"message":"Image not found"}), 400
    
# addPerson(name, email, spire, imageStr)

if __name__ == '__main__':
    app.run(debug=True)
