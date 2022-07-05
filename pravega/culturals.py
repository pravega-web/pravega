from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for, send_file
        )
blueprint = Blueprint('culturals', __name__,template_folder='/templates', url_prefix="/culturals")
import razorpay
import pymongo

razorpay_secret_key = "lmao"


@blueprint.route("/")
def show_culturals_menu():
    return render_template("culturals/culturals_menu.html");

@blueprint.route("/<event_name>")
def show_culturals_event(event_name):
    return render_template(f"culturals/{event_name}.html");
@blueprint.route("/lasya/rules")
def show_lasya_tc():
    return send_file('files/Lasya_T&C.docx')
@blueprint.route("/lasya/register")
def lasya_redirect():
    return render_template("/culturals/lasya.html");

@blueprint.route("/lasya/individualregister", methods=("GET","POST"))
def lasya_ind_culturals_register():
    event_name = "lasya"
    amount = 10000
    if request.method == "GET":
        return render_template("culturals/registration/registration_ind_lasya.html")

    if request.method == "POST":
        details = { "name" : request.form['name'],
                    "age" : request.form['age'],
                    "school" : request.form['school'],
                    "email" : request.form['email'],
                    "instagram" : request.form['instagram'],
                    "phone" : request.form['mobile'],
                    "address" : request.form['address'],
                    "additional_info" : request.form['addinfo'],
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
        existing = mycol.find_one({ "email" : request.form['email'] })

        paydb = myclient['payments']
        paycol = paydb[event_name]


        if existing is None:
            razorpay_client.payment.capture(payment_id, amount)
            details['payment_id'] = payment_id
            pay_details = razorpay_client.payment.fetch(payment_id)
            paycol.insert_one(pay_details)
            details['payment_status'] = pay_details['status']
            flash(f"Payment ID:{payment_id}")
            if pay_details['status'] == 'captured':
                flash("Payment Successful")
            else:
                flash("Payment not confirmed, Contact us")
            x = mycol.insert_one(details)
            flash("Registered successfully!!")
        else :
            details['payment_id'] = payment_id
            pay_details = razorpay_client.payment.fetch(payment_id)
            paycol.insert_one(pay_details)
            details['payment_status'] = pay_details['status']
            flash(f"Payment ID:{payment_id}")
            flash("Payment not confirmed")
            flash("Email of participant already registered ask for refund on email if paid twice")
            myclient.close()
            return render_template(f"registration_message.html")

        myclient.close()
        return render_template(f"registration_message.html")

@blueprint.route("/lasya/teamregister", methods=("GET","POST"))
def lasya_team_culturals_register():
    event_name = "lasya"
    amount = 50000
    if request.method == "GET":
        return render_template("culturals/registration/registration_team_lasya.html")

    if request.method == "POST":
        details = { "name" : request.form['name'],
                    "age" : request.form['age'],
                    "team" : request.form['team'],
                    "number" : request.form['number'],
                    "school" : request.form['school'],
                    "email" : request.form['email'],
                    "instagram" : request.form['instagram'],
                    "phone" : request.form['mobile'],
                    "address" : request.form['address'],
                    "additional_info" : request.form['addinfo'],
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
        existing = mycol.find_one({ "email" : request.form['email'] })

        paydb = myclient['payments']
        paycol = paydb[event_name]


        if existing is None:
            razorpay_client.payment.capture(payment_id, amount)
            details['payment_id'] = payment_id
            pay_details = razorpay_client.payment.fetch(payment_id)
            paycol.insert_one(pay_details)
            details['payment_status'] = pay_details['status']
            flash(f"Payment ID:{payment_id}")
            if pay_details['status'] == 'captured':
                flash("Payment Successful")
            else:
                flash("Payment not confirmed, Contact us")
            x = mycol.insert_one(details)
            flash("Registered successfully!!")
        else :
            details['payment_id'] = payment_id
            pay_details = razorpay_client.payment.fetch(payment_id)
            paycol.insert_one(pay_details)
            details['payment_status'] = pay_details['status']
            flash(f"Payment ID:{payment_id}")
            flash("Payment not confirmed")
            flash("Email of participant already registered ask for refund on email if paid twice")
            myclient.close()
            return render_template(f"registration_message.html")

        myclient.close()
        return render_template(f"registration_message.html")

@blueprint.route("generic/register", methods=("GET", "POST"))
def generic_unpaid_culturals_register():
    event_name = "generic"
    if request.method == "GET":
        return render_template(f"registration/registration_{event_name}.html")
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
        mycol = mydb[event_name]
        #Checking for duplicate mobile numbers
        existing = mycol.find_one({ "participant1_email" : request.form['emailp1'] })

        if existing is None:
            x = mycol.insert_one(details)
            flash("Registered successfully!!")
        if existing is not None :
            flash("Email of participant 1 already registered")
            myclient.close()
            return render_template(f"registration_{event_name}.html")
        myclient.close()

        flash("Email of participant 1 already registered")
        return render_template(f"registration_{event_name}.html")

@blueprint.route("generic/paid-register", methods=("GET","POST"))
def generic_paid_culturals_register():
    event_name = "paid_generic"
    amount = 20000
    if request.method == "GET":
        return render_template(f"registration/registration_{event_name}.html")

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
            if pay_details['status'] == 'captured':
                flash("Payment Successful")
            else:
                flash("Payment not confirmed, Contact us")
            x = mycol.insert_one(details)
            flash("Registered successfully!!")
        else :
            details['payment_id'] = payment_id
            pay_details = razorpay_client.payment.fetch(payment_id)
            paycol.insert_one(pay_details)
            details['payment_status'] = pay_details['status']
            flash(f"Payment ID:{payment_id}")
            flash("Payment not confirmed")
            flash("Email of participant 1 already registered ask for refund on email if paid twice")
            myclient.close()
            return render_template(f"registration_{event_name}.html")

        myclient.close()
        return render_template(f"registration_{event_name}.html")
