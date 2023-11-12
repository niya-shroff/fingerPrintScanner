from flask import Flask, request
import base64
import json
app = Flask(__name__)

""" listener.py
    This program hosts a server with Flask, takes in a base 64 encoded JSON file from a POST request, 
    and decodes it back into an image.

    As long as this is running (on same hotspot as Pi), any images of faces will be written in a new test.jpg file.

    *** May want to make sure we don't get a ton of duplicate test.jpg files later ***
"""
# Allow POST requests
@app.route("/", methods=["GET", "POST"])
# if POST request, take as JSON and decode back into image
def decode_image():
    if request.method == "POST":
        img = request.json
        image = base64.b64decode(img['image'])
        with open(r'test.jpg', 'wb') as f: # change file name
            f.write(image)
            
    return "Completed! Image is now loaded as test.jpg!" # change name 

if __name__ == "__main__":
    app.run() 
