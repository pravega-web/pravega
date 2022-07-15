from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for
        )
import pymongo
import razorpay
blueprint = Blueprint('recreational',__name__, template_folder="templates/", url_prefix='/recreational')

razorpay_secret_key='lmao'
fromaddr = "core@pravega.org"
emailsecretpassword = 'emailpassword'


@blueprint.route('/')
def show_recreational():
    return render_template("recreational/recreational_menu.html")
@blueprint.route('/<event_name>')
def show_recreationalpage(event_name):
    return render_template(f"recreational/{event_name}.html")
@blueprint.route("/generic_free/register", methods=("GET","POST"))
def register_for_free ():
    event_name = "generic_free"
    if request.method == "GET":
        return render_template(f"recreational/registration/registration_{event_name}.html");
    if request.method == "POST":
        details = { "participant1_name" : request.form['participant1'],        # change this as per form
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
            return render_template("registration_message.html")
        myclient.close()

        return render_template("registration_message.html")

@blueprint.route("/generic_paid/register", methods=("GET", "POST"))
def register_for_paid ():
    event_name = "generic_paid"
    amount = 20000
    g.user = amount
    if request.method == "GET":
        return render_template(f"recreational/registration/registration_{event_name}.html")

    if request.method == "POST":
        details = { "participant1_name" : request.form['participant1'],  # change this
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

@blueprint.route("/qsac/register", methods=("GET","POST"))
def register_for_qsac ():
    event_name = "qsac"
    amount = 10000
    g.user = amount
    if request.method == "GET":
        return render_template(f"recreational/registration/registration_{event_name}.html")

    if request.method == "POST":
        details = { "participant_name" : request.form['name'],  # change this
                    "email_id" : request.form['email1'],
                    "dob" : request.form['dob'],
                    "phone" : request.form['mobile1'],
                    "lichessid" : request.form['lichessid'],
                    "gender" : request.form['gender'],
                    "nationality" : request.form['nation'],
                    "fideid" : request.form['fideid'],
                    "fiderating" : request.form['fiderating'],
                    "school" : reques.form['school'],
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
        existing = mycol.find_one({ "email_id" : request.form['email1'] })

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
                import smtplib
                from email.mime.multipart import MIMEMultipart
                from email.mime.text import MIMEText
                from email.mime.base import MIMEBase
                from email import encoders

                toaddr = details['email_id']
                participantname = details['participant_name']
                msg = MIMEMultipart()
                msg['From'] = "Pravega IISc"
                msg['To'] = toaddr
                msg['Subject'] = "Lichess team link for Q- sac pre- pravega event"
                body = """Dear Participant, 
Thanks for registering for Q-Sac pre pravega event.  You are requested to send a request to join the lichess team from your given username by clicking on the below link:
https://lichess.org/team/q-sac-pre-pravega-chess-tournament-team

Once you send a request to join the team, the organizors will accept you in the team, subject to verification of your details. Please do this ASAP as the organizers need time to verify the details.
Thanks and hope to see you on the 31st of July at 6 PM. All the best. 

THIS MAIL IS AUTOGENERATED. DO NOT REPLY TO THIS MAIL.
For any queries, mail shubhprakash@iisc.ac.in

Regards, 
Team Q-Sac"""
                msg.attach(MIMEText(body, 'plain'))

                # creates SMTP session
                s = smtplib.SMTP('smtp.gmail.com', 587)

                # start TLS for security
                s.starttls()

                # Authentication
                s.login(fromaddr, emailsecretpassword)

                # message to be sent
                message = msg.as_string()

                # sending the mail
                s.sendmail(fromaddr, toaddr, message)

                # terminating the session
                s.quit()
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
