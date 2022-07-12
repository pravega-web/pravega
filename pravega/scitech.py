from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for
        )
import pymongo
import razorpay
blueprint = Blueprint('scitech',__name__, template_folder="templates/", url_prefix='/scitech')

razorpay_secret_key='lmao'

@blueprint.route('/')
def show_scitech():
    return render_template("scitech/scitech_menu.html")
@blueprint.route('/<event_name>')
def show_scitechpage(event_name):
    return render_template(f"scitech/{event_name}.html")
@blueprint.route("/chemenigma/register", methods=("GET","POST"))
def register_for_chemenigma2 ():
    event_name = "chemenigma"
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html");
    if request.method == "POST":
        details = { "participant1_name" : request.form['participant1'],
                    "participant2_name" : request.form['participant2'],
                    "team_name" : request.form['team'],
                    "participant1_class" : request.form['clsp1'],
                    "participant2_class" : request.form['clsp2'],
                    "participant1_school" : request.form['school1'],
                    "participant2_school" : request.form['school2'],
                    "participant1_email" : request.form['emailp1'],
                    "participant2_email" : request.form['emailp2'],
                    "participant1_phone" : request.form['mobile1'],
                    "participant2_phone" : request.form['mobile2']
                    }
        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['registrations']
        mycol = mydb['chemenigma']
        #Checking for duplicate mobile numbers
        existing = mycol.find_one({ "participant1_email" : request.form['emailp1'] })

        if existing is None:
            x = mycol.insert_one(details)
            flash("Registered successfully!!")
        if existing is not None :
            flash("Email of participant 1 already registered")
            myclient.close()
            return render_template("registration_message.html")
        myclient.close()

        return render_template("registration_message.html")

@blueprint.route("/chemenigma/register/post", methods=("GET","POST"))
def register_for_chemenigma ():
    event_name = "chemenigma"
    if request.method == "POST":
        details = { "participant1_name" : request.form['participant1'],
                    "participant2_name" : request.form['participant2'],
                    "team_name" : request.form['team'],
                    "participant1_class" : request.form['clsp1'],
                    "participant2_class" : request.form['clsp2'],
                    "participant1_school" : request.form['school1'],
                    "participant2_school" : request.form['school2'],
                    "participant1_email" : request.form['emailp1'],
                    "participant2_email" : request.form['emailp2'],
                    "participant1_phone" : request.form['mobile1'],
                    "participant2_phone" : request.form['mobile2']
                    }
        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['registrations']
        mycol = mydb['chemenigma']
        #Checking for duplicate mobile numbers
        existing = mycol.find_one({ "participant1_email" : request.form['emailp1'] })

        if existing is None:
            x = mycol.insert_one(details)
            flash("Registered successfully!!")
        if existing is not None :
            flash("Email of participant 1 already registered")
            myclient.close()
            return render_template("registration_message.html")
        myclient.close()

        return render_template("registration_message.html")

@blueprint.route("/enumeration/register", methods=("GET", "POST"))
def register_for_enumeration ():
    event_name = "enumeration"
    amount = 20000
    g.user = amount
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html")

    if request.method == "POST":
        details = { "participant1_name" : request.form['participant1'],
                    "participant2_name" : request.form['participant2'],
                    "team_name" : request.form['team'],
                    "participant1_school" : request.form['school1'],
                    "participant2_school" : request.form['school2'],
                    "participant1_email" : request.form['emailp1'],
                    "participant2_email" : request.form['emailp2'],
                    "participant1_phone" : request.form['mobile1'],
                    "participant2_phone" : request.form['mobile2'],
                    "payment_id" : None,
                    "payment_status" : "Unknown"
                    }
        # Authenticating payments
        razorpay_client = razorpay.Client(auth=("rzp_live_jEr5MWFDFyEN8f",razorpay_secret_key))
        payment_id = request.form['razorpay_payment_id']


        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient['registrations']
        mycol = mydb[event_name]


        #Checking for duplicate email numbers
        existing = mycol.find_one({ "participant1_email" : request.form['emailp1'] })

        paydb = myclient['payments']
        paycol = paydb[event_name]


        if existing is None:
            razorpay_client.payment.capture(payment_id, amount)
            details['payment_id'] = payment_id
            pay_details = razorpay_client.payment.fetch(payment_id)
            paycol.insert_one(pay_details)
            details['payment_status'] = pay_details['status']
            flash(f"Payment ID:{payment_id}")
            x = mycol.insert_one(details)
            if pay_details['status'] == 'captured':
                flash("Payment Successful")
            else:
                flash("Payment not confirmed, Contact us")
            flash("Registered successfully!!")
        else :
            details['payment_id'] = payment_id
            pay_details = razorpay_client.payment.fetch(payment_id)
            paycol.insert_one(pay_details)
            details['payment_status'] = pay_details['status']
            flash(f"Payment ID:{payment_id}")
            flash("Payment not confirmed")
            flash("Email of participant 1 already registered")
            myclient.close()
            return render_template("/registration_message.html")

        myclient.close()
        return render_template("/registration_message.html")



@blueprint.route('/astrowiz/register', methods=("GET", "POST"))
def register_astrowiz():
    event_name = "astrowiz"
    if request.method == "GET":
        return render_template('scitech/registration/registration_astrowiz.html')
    if request.method == "POST":
        details = { "participant_name" : request.form['participant'],
                    "participant_school" : request.form['school'],
                    "participant_class" : request.form['clsp'],
                    "participant_email" : request.form['email'],
                    "participant_phone" : request.form['mobile']
                    }
        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['registrations']
        mycol = mydb[event_name]
        #Checking for duplicate mobile numbers
        existing = mycol.find_one({ "participant_email" : request.form['email'] })

        if existing is None:
            x = mycol.insert_one(details)
            flash("Registered successfully!!")
        if existing is not None :
            flash("Could not register!!")
            flash("Email of participant already registered")
            myclient.close()
            return render_template("registration_message.html")
        myclient.close()
        return render_template("registration_message.html")

@blueprint.route("/decoherence/register", methods=("GET","POST"))
def register_for_decoherence ():
    event_name = "decoherence"
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html");
    if request.method == "POST":
        details = { "participant1_name" : request.form['participant'],
                    "participant1_class" : request.form['clsp'],
                    "participant1_school" : request.form['school'],
                    "participant1_email" : request.form['email'],
                    "participant1_phone" : request.form['mobile'],
                    "participant2_name" : request.form['participant2'],
                    "participant2_email" : request.form['email2']
                    }
        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['registrations']
        mycol = mydb[event_name]
        #Checking for duplicate mobile numbers
        existing = mycol.find_one({ "participant1_email" : request.form['email'] })

        if existing is None:
            x = mycol.insert_one(details)
            flash("Registered successfully!!")
        if existing is not None :
            flash("Email of participant already registered")
            myclient.close()
            return render_template("registration_message.html")
        myclient.close()

        return render_template("registration_message.html")

@blueprint.route("/bioblitz/register", methods=("GET","POST"))
def register_for_bioblitz ():
    event_name = "bioblitz"
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html");
    if request.method == "POST":
        details = { "participant1_name" : request.form['participant'],
                    "participant1_email" : request.form['email'],
                    "participant1_phone" : request.form['mobile'],
                    "participant1_school" : request.form['school'],
                    "participant1_class" : request.form['clsp'],
                    "participant1_city" : request.form['city'],
                    "participant2_name" : request.form['participant2'],
                    "participant2_email" : request.form['email2'],
                    "participant2_phone" : request.form['mobile2'],
                    "participant2_school" : request.form['school2'],
                    "participant2_class" : request.form['clsp2'],
                    "participant2_city" : request.form['city2'],
                    "participant3_name" : request.form['participant3'],
                    "participant3_email" : request.form['email3'],
                    "participant3_phone" : request.form['mobile3'],
                    "participant3_school" : request.form['school3'],
                    "participant3_class" : request.form['clsp3'],
                    "participant3_city" : request.form['city3'],
                    }
        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['registrations']
        mycol = mydb[event_name]
        #Checking for duplicate mobile numbers
        existing = mycol.find_one({ "participant1_email" : request.form['email'] })

        if existing is None:
            x = mycol.insert_one(details)
            flash("Registered successfully!!")
        if existing is not None :
            flash("Email of participant already registered")
            myclient.close()
            return render_template("registration_message.html")
        myclient.close()

        return render_template("registration_message.html")

@blueprint.route("/palebluedot/register", methods=("GET","POST"))
def register_for_palebluedot():
    event_name = "palebluedot"
    amount = 5000
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html");
    if request.method == "POST":
        details = { "team_name" : request.form['team'],
                    "team_location" : request.form['location'],
                    "come" : request.form['come'],
                    "team_size" : request.form['teamsize'],
                    "school" : request.form['school'],
                    "class" : request.form["clsp"],
                    "p1" : request.form["participant1"],
                    "email1" : request.form["email1"],
                    "participant1_phone" : request.form['mobile1'],
                    "p2" : request.form["participant2"],
                    "email2" : request.form["email2"],
                    "participant2_phone" : request.form['mobile2'],
                    }
                # Authenticating payments
        razorpay_client = razorpay.Client(auth=("rzp_live_jEr5MWFDFyEN8f",razorpay_secret_key))
        payment_id = request.form['razorpay_payment_id']


        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient['registrations']
        mycol = mydb[event_name]


        #Checking for duplicate email numbers
        existing = mycol.find_one({ "participant1_email" : request.form['emailp1'] })

        paydb = myclient['payments']
        paycol = paydb[event_name]


        if existing is None:
            razorpay_client.payment.capture(payment_id, amount)
            details['payment_id'] = payment_id
            pay_details = razorpay_client.payment.fetch(payment_id)
            paycol.insert_one(pay_details)
            details['payment_status'] = pay_details['status']
            flash(f"Payment ID:{payment_id}")
            x = mycol.insert_one(details)
            if pay_details['status'] == 'captured':
                flash("Payment Successful")
            else:
                flash("Payment not confirmed, Contact us")
        else :
            details['payment_id'] = payment_id
            pay_details = razorpay_client.payment.fetch(payment_id)
            paycol.insert_one(pay_details)
            details['payment_status'] = pay_details['status']
            flash(f"Payment ID:{payment_id}")
            flash("Payment not confirmed")
            flash("Email of participant 1 already registered ask for refund on email if paid twice")
            myclient.close()
            return render_template("/registration_message.html")

        myclient.close()
        return render_template("/registration_message.html")
