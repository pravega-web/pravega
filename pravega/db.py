import pymongo


def get_db(event):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient["registrations"]
    return mydb['event']

def close_db(db):
    db.close()
