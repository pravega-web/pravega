from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for, send_file
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
    try:
        return render_template(f"scitech/{event_name}.html")
    except:
        return render_template("pagenotfound.html")

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

            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from email.mime.base import MIMEBase
            from email import encoders

            toaddr = request.form['email']
            participantname = details['participant_name']
            fromaddr = "core@pravega.org"
            msg = MIMEMultipart()
            msg['From'] = "Pravega IISc"
            msg['To'] = toaddr
            msg['Subject'] = "Registration for Astrowiz by Pravega IISc"
            body = f"Congratulations, {participantname} you have successfully registered for Astrowiz by Pravega.\n Registered details are:\n Name: {details['participant_name']} \n School: {details['participant_school']} \n Class: {details['participant_class']} \n Email: {details['participant_email']} \n Phone: {details['participant_phone']} \n Best of luck for your quiz on 16July \n Thanks\n Team Pravega"
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
    amount = 10000
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
        existing = mycol.find_one({ "email1" : request.form['email1'] })

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
@blueprint.route("/straingerthings/register", methods=("GET","POST"))
def register_for_straingerthings ():
    event_name = "straingerthings"
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html");
    if request.method == "POST":
        details = { "participant1_name" : request.form['participant_name'],
                    "participant1_class" : request.form['clsp'],
                    "participant1_school" : request.form['school'],
                    "participant1_email" : request.form['email'],
                    "participant1_phone" : request.form['mobile']
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
@blueprint.route("/badadhochypotheses/register", methods=("GET","POST"))
def register_for_badhypotheses():
    event_name = "badadhochypotheses"
    amount = 10000
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html");
    if request.method == "POST":
        details = {
                    "participant_name" : request.form["participant_name"],
                    "participant_age" : request.form["age"],
                    "participant_school" : request.form['school'],
                    "participant_address" : request.form['address'],
                    "participant_email" : request.form["email"],
                    "participant_phone" : request.form['mobile'],
                    "participant_more" : request.form['more']
                    }
                # Authenticating payments
        # razorpay_client = razorpay.Client(auth=("rzp_live_jEr5MWFDFyEN8f",razorpay_secret_key))
        # payment_id = request.form['razorpay_payment_id']


        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient['registrations']
        mycol = mydb[event_name]


        #Checking for duplicate email numbers
        existing = mycol.find_one({ "participant_email" : request.form['email'] })

        # paydb = myclient['payments']
        # paycol = paydb[event_name]


        if existing is None:
            # razorpay_client.payment.capture(payment_id, amount)
            details['payment_id'] = "none"
            # pay_details = razorpay_client.payment.fetch(payment_id)
            # paycol.insert_one(pay_details)
            # details['payment_status'] = pay_details['status']
            details['payment_status'] = "none"
            # flash(f"Payment ID:{payment_id}")
            x = mycol.insert_one(details)
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from email.mime.base import MIMEBase
            from email import encoders

            toaddr = request.form['email']
            participantname = details['participant_name']
            fromaddr = "core@pravega.org"
            msg = MIMEMultipart()
            msg['From'] = "Pravega IISc"
            msg['To'] = toaddr
            msg['Subject'] = "Registration for Bad Ad Hoc Hypotheses by Pravega IISc"
            body = f"""Hello Enthusiast,
Thank you for registering for Bad Ad Hoc Hypotheses! Please take a good look at the brochure at pravega.org/files/BAH_Brochure.pdf for all the details about the form and structure of the event. Mail us your alpha-presentation and teaser video at bah.pravega@gmail.com.  Reach out to us if you have any other queries. We will send you a confirmation mail within one day once we receive your entry.
Hope you have a fun time concocting your hypothesis!

Team BAH'22


Registered details are:
Name:   {details['participant_name']}
Age:    {details['participant_age']}
Address:    {details['participant_address']}
School: {details['participant_school']}
Email:  {details['participant_email']}
Phone:  {details['participant_phone']}
More details/Comments:  {details['participant_more']}

THIS MAIL IS AUTOGENERATED. DO NOT REPLY TO THIS MAIL.
For any queries, mail bah.pravega@gmail.com"""
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

            flash("Registered Successfully!!")
            flash("Check the registered email id. PS: Don't forget to check your junk mail!!")
        else :
            details['payment_id'] = "Error"
            details['payment_status'] = "None"
            flash("Registration not Confirmed")
            flash("Email of participant 1 already registered ask for refund on email if paid twice")
            myclient.close()
            return render_template("/registration_message.html")

        myclient.close()
        return render_template("/registration_message.html")

@blueprint.route("/pravegainnovationsummit/rules")
def sendpisrules():
    return send_file("files/PIS_RulesAndRegulations.pdf")
@blueprint.route("/pravegainnovationsummit/register", methods=("GET", "POST"))
def register_for_pis ():
    event_name = "pravegainnovationsummit"
    amount = 200000
    g.user = amount
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html")

    if request.method == "POST":
        details = {
                    "team_name" : request.form['team'],
                    "participant1_name" : request.form['participant1'],
                    "participant2_name" : request.form['participant2'],
                    "participant3_name" : request.form['participant3'],
                    "participant4_name" : request.form['participant4'],
                    "participant5_name" : request.form['participant5'],
                    "participant_address" : request.form['address'],
                    "participant_email" : request.form['email'],
                    "participant_phone" : request.form['mobile'],
                    "payment_id" : None,
                    "payment_status" : "Unknown"
                    }
        # Authenticating payments
        # razorpay_client = razorpay.Client(auth=("rzp_live_jEr5MWFDFyEN8f",razorpay_secret_key))
        # payment_id = request.form['razorpay_payment_id']


        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient['registrations']
        mycol = mydb[event_name]


        #Checking for duplicate email numbers
        existing = mycol.find_one({ "participant_email" : request.form['email'] })

        # paydb = myclient['payments']
        # paycol = paydb[event_name]


        if existing is None:
            # razorpay_client.payment.capture(payment_id, amount)
            # details['payment_id'] = payment_id
            # pay_details = razorpay_client.payment.fetch(payment_id)
            # paycol.insert_one(pay_details)
            # details['payment_status'] = pay_details['status']
            # flash(f"Payment ID:{payment_id}")
            x = mycol.insert_one(details)
            # if pay_details['status'] == 'captured':
            #     flash("Payment Successful")
            # else:
            #     flash("Payment not confirmed, Contact us")
            flash("Registered successfully!!")
        else :
            # details['payment_id'] = payment_id
            # pay_details = razorpay_client.payment.fetch(payment_id)
            # paycol.insert_one(pay_details)
            # details['payment_status'] = pay_details['status']
            # flash(f"Payment ID:{payment_id}")
            # flash("Payment not confirmed")
            flash("Email of participant 1 already registered")
            myclient.close()
            return render_template("/registration_message.html")

        myclient.close()
        return render_template("/registration_message.html")

@blueprint.route("/robowars/register", methods=("GET","POST"))
def register_for_robowars ():
    event_name = "robowars"
    amount = 80000
    g.user = amount
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html")

    if request.method == "POST":
        details = { "team_name" : request.form["team"],
                    "participant_name" : request.form['leader'],  # change this
                    "email_id" : request.form['email'],
                    "phone" : request.form['mobile'],
                    }
        # Authenticating payments
        razorpay_client = razorpay.Client(auth=("rzp_live_jEr5MWFDFyEN8f",razorpay_secret_key))
        payment_id = request.form['razorpay_payment_id']


        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient['registrations']
        mycol = mydb[event_name]


        #Checking for duplicate email numbers
        existing = mycol.find_one({ "email_id" : request.form['email'] })

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
                fromaddr = "core@pravega.org"
                msg = MIMEMultipart()
                msg['From'] = "Pravega IISc"
                msg['To'] = toaddr
                msg['Subject'] = "Registration for Robowars - Pravega 2022"
                body = """Hey there!
Your registration has been accepted, welcome to Ragnarok Robowar. All further communication from our side shall be carried out on our discord server. If you do not already have a Discord account, you are requested to make one. Here’s the access link:
https://discord.gg/7crvzUAeG8
For any help in building the robot or inquiry about the rules, you should check out our help and tutorial channels.
The server is exclusive to registered participants of the event and a place for participants to interact with each other and with the organizers.
As such, please do not share this invite link with anyone else.

THIS MAIL IS AUTO-GENERATED. DO NOT REPLY TO THIS MAIL.
For unresolved queries, feel free to contact us @ ragnarokrobowar@gmail.com"""
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

@blueprint.route("/exhibitions/register", methods=("GET","POST"))
def register_for_exhibitions ():
    event_name = "exhibitions"
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html");
    if request.method == "POST":
        details = { "team_name" : request.form['team'],
                    "participant1_name" : request.form['name1'],
                    "participant1_institue" : request.form['institute1'],
                    "participant1_email" : request.form['email1'],
                    "participant1_phone" : request.form['mobile1'],
                    "participant2_name" : request.form['name2'],
                    "participant2_institue" : request.form['institute2'],
                    "participant2_email" : request.form['email2'],
                    "participant2_phone" : request.form['mobile2'],
                    "participant3_name" : request.form['name3'],
                    "participant3_institue" : request.form['institute3'],
                    "participant3_email" : request.form['email3'],
                    "participant3_phone" : request.form['mobile3'],
                    "team-coming" : request.form['come']
                    }
        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['registrations']
        mycol = mydb[event_name]
        #Checking for duplicate mobile numbers
        existing = mycol.find_one({ "participant1_email" : request.form['email1'] })

        if existing is None:
            x = mycol.insert_one(details)
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            from email.mime.base import MIMEBase
            from email import encoders

            toaddr = request.form['email1']
            participantname = details['participant1_name']
            fromaddr = "core@pravega.org"
            msg = MIMEMultipart()
            msg['From'] = "Pravega IISc"
            msg['To'] = toaddr
            msg['Subject'] = "Registration for Exhibitions by Pravega IISc"
            body = f"""Hello Enthusiast,
Thank you for registering for IISc Exhibitions, Please read the rules( https://www.pravega.org/files/exhibitionrules ) carefully.
All further details will be relayed to you via email.
Team Exhibition


Registered details are:
Team Name : {request.form['team']}
Participant1 Name : {request.form['name1']}
Participant1 Institue : {request.form['institute1']}
Participant1 Email : {request.form['email1']}
Participant1 Phone : {request.form['mobile1']}
Participant2 Name : {request.form['name2']}
Participant2 Institue : {request.form['institute2']}
Participant2 Email : {request.form['email2']}
Participant2 Phone : {request.form['mobile2']}
Participant3 Name : {request.form['name3']}
Participant3 Institue : {request.form['institute3']}
Participant3 Email : {request.form['email3']}
Participant3 Phone : {request.form['mobile3']}
Can come to Bangalore : {request.form['come']}


THIS MAIL IS AUTOGENERATED. DO NOT REPLY TO THIS MAIL.
For any queries, mail exhibitions2022.pravega@gmail.com
ThankYou"""
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
            flash("Check the email of the first participant. PS. Don't forget to check your junk mail!!")
        if existing is not None :
            flash("Email of participant already registered")
            myclient.close()
            return render_template("registration_message.html")
        myclient.close()

        return render_template("registration_message.html")

@blueprint.route("/whatwoulddarwindo/register", methods=("GET","POST"))
def register_for_wwdd():
    event_name = "whatwoulddarwindo"
    amount = 10000
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html");
    if request.method == "POST":
        details = {
                    "participant_name" : request.form["name"],
                    "participant_age" : request.form["age"],
                    "participant_class" : request.form['class'],
                    "participant_address" : request.form['address'],
                    "participant_email" : request.form["email"],
                    "participant_phone" : request.form['mobile'],
                    "participant_more" : request.form['more']
                    }
                # Authenticating payments
        razorpay_client = razorpay.Client(auth=("rzp_live_jEr5MWFDFyEN8f",razorpay_secret_key))
        payment_id = request.form['razorpay_payment_id']


        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient['registrations']
        mycol = mydb[event_name]


        #Checking for duplicate email numbers
        existing = mycol.find_one({ "participant_email" : request.form['email'] })

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

                toaddr = request.form['email']
                participantname = details['participant_name']
                fromaddr = "core@pravega.org"
                msg = MIMEMultipart()
                msg['From'] = "Pravega IISc"
                msg['To'] = toaddr
                msg['Subject'] = "Registration for What Would Darwin Do by Pravega IISc"
                body = f"""Hello Enthusiast,
Thank you for registering for WWDD! Please take a good look at the brochure at pravega.org/files/wwdd_brochure.pdf for all the details about the form and structure of the event. Reach out to us if you have any other queries.

Team WWDD'22


Registered details are:
Name:   {details['participant_name']}
Age:    {details['participant_age']}
Address:    {details['participant_address']}
Grade: {details['participant_class']}
Email:  {details['participant_email']}
Phone:  {details['participant_phone']}
More details/Comments:  {details['participant_more']}

THIS MAIL IS AUTOGENERATED. DO NOT REPLY TO THIS MAIL.
For any queries, mail wwdd.pravega@gmail.com"""
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

                flash("Payment Successful")
                flash("Check the registered email id. PS: Don't forget to check your junk mail!!")
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

@blueprint.route("/honourcode/register", methods=("GET","POST"))
def register_for_honourcode():
    event_name = "honourcode"
    if request.method == "GET":
        return render_template(f"scitech/registration/registration_{event_name}.html")
    if request.method == "POST":
        details = {
                    "participant_name" : request.form["participant_name"],
                    "participant_age" : request.form["age"],
                    "participant_school" : request.form['school'],
                    "participant_email" : request.form["email"],
                    "participant_phone" : request.form['mobile'],
                    "codechef" : request.form['handle']
                    }
                # Authenticating payments
        # razorpay_client = razorpay.Client(auth=("rzp_live_jEr5MWFDFyEN8f",razorpay_secret_key))
        # payment_id = request.form['razorpay_payment_id']


        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")

        mydb = myclient['registrations']
        mycol = mydb[event_name]


        #Checking for duplicate email numbers
        existing = mycol.find_one({ "participant_email" : request.form['email'] })

        # paydb = myclient['payments']
        # paycol = paydb[event_name]


        if existing is None:
            # razorpay_client.payment.capture(payment_id, amount)
            details['payment_id'] = "none"
            # pay_details = razorpay_client.payment.fetch(payment_id)
            # paycol.insert_one(pay_details)
            # details['payment_status'] = pay_details['status']
            details['payment_status'] = "none"
            # flash(f"Payment ID:{payment_id}")
            x = mycol.insert_one(details)

            flash("Registered Successfully!!")
        else :
            details['payment_id'] = "Error"
            details['payment_status'] = "None"
            flash("Registration not Confirmed")
            flash("Email of participant 1 already registered")
            myclient.close()
            return render_template("/registration_message.html")

        myclient.close()
        return render_template("/registration_message.html")