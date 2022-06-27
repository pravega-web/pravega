import pymongo


def get_db(event):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient["registrations"]
    return mydb['event']

def close_db(db):
    db.close()

# pymongo functions to copy in the files

def dumbfunction():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient['registrations']
    mycol = mydb['chemenigma']
    #Checking for duplicate mobile numbers
    existing = mycol.find_one({ "praticipant1_email" : request.form['emailp1'] })

    if existing is None:
        x = mycol.insert_one(details)
        flash("Registered successfully!!")
    if existing is not None :
        flash("Email of participant 1 already registered")
        myclient.close()
        return render_template(f"registration_{event_name}.html")
    myclient.close()




    paydb=myclient['payments']
    paycol = paydb['nameofevent']
