from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for, send_file
        )
import pymongo
import razorpay
blueprint = Blueprint('speakers',__name__, template_folder="templates/speakers/", url_prefix='/speakers')

@blueprint.route('/<speaker>')
def register_speaker(speaker):
    event_name = speaker
    if request.method == "GET":
        return render_template(speaker+'.html')
    if request.method == "POST":
        details = { "event" : speaker,
                    "name" : request.form['name'],
                    "organisation" : request.form['organisation'],
                    "email" : request.form['email'],
                    "mobile" : request.form['mobile']
                    }
        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['registrations']
        mycol = mydb[event_name]
        #Checking for duplicate mobile numbers
        existing = mycol.find_one({ "email" : request.form['email'] })

        if existing is None:
            x = mycol.insert_one(details)

            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from email.mime.base import MIMEBase
            from email import encoders

            toaddr = request.form['email']
            participantname = details['name']
            fromaddr = "core@pravega.org"
            msg = MIMEMultipart()
            msg['From'] = "Pravega IISc"
            msg['To'] = toaddr
            msg['Subject'] = "Registration for talk by Ankur Warikoo during Pravega IISc"
            body = f"Hi {participantname},\nYou've successfully registered for the talk by Ankur Warikoo on 2nd September, 12:30pm.\nRegistered phone number: {details['mobile']} \n\n Thanks\n Team Pravega"
            msg.attach(MIMEText(body, 'plain'))

            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)

            # start TLS for security
            s.starttls()

            # Authentication
            s.login("core@pravega.org", "emailsecretpassword")

            # message to be sent
            message = msg.as_string()

            # sending the mail
            s.sendmail(fromaddr, toaddr, message)

            # terminating the session
            s.quit()
            flash("Registered successfully!!")
            flash("Check you email for confirmation. PS: check your junk mail folder as well")
        if existing is not None :
            flash("Could not register!!")
            flash("Email of participant already registered")
            myclient.close()
            return render_template("registration_message.html")
        myclient.close()
        return render_template("registration_message.html")