from pymongo.mongo_client import MongoClient
client = MongoClient("mongodb+srv://mkandeshwara:1234@printscanner.mgav5zb.mongodb.net/?retryWrites=true&w=majority")

def addPerson(name, email):
    person = {
        "name": name,
        # "SpireID": spid,
        "email": email
    }
    db = client["people"]
    col = db["students"]
    col.insert_one(person)