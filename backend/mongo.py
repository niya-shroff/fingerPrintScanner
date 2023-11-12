from pymongo.mongo_client import MongoClient
client = MongoClient("mongodb+srv://mkandeshwara:1234@printscanner.mgav5zb.mongodb.net/?retryWrites=true&w=majority")

def addPerson(name, email, spire, imageStr):
    person = {
        "name": name,
        "email": email, 
        "spire": spire,
        "image": imageStr,
    }
    db = client["people"]
    col = db["students"]
    col.insert_one(person)

addPerson("Niya", "shroffniya@gmail.com", "33200071", "hi")