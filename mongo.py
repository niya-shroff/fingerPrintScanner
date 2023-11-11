from pymongo.mongo_client import MongoClient
client = MongoClient("mongodb+srv://mkandeshwara:1234@printscanner.mgav5zb.mongodb.net/?retryWrites=true&w=majority")

def addPerson(print, name, spid, email, type):
    person = {
        "print": print,
        "name": name,
        "SpireID": spid,
        "email": email,
        "type": type
    }
    db = client["people"]
    if(type == "student"):
        col = db["students"]
        col.insert_one(person)
    elif(type == "faculty"):
        col = db["faculty"]
        col.insert_one(person)