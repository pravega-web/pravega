"""Implements event webpages including registration.

Variable `blueprint`: a `flask.Blueprint` for the event pages and event
registration pages."""

# Assumptions about how to find external data (can be changed as needed):
# + For each event accessible at URL "/events/<event_name>":
#   + file templates/events/<event_name>.html: Jinja template for that page
#   + file data/events/<event_name>.json: JSON file, available in the Jinja
#     template as variable `event`

from json import load as load_json
from flask import Blueprint, render_template,request, flash, redirect, url_for
import pymongo

blueprint = Blueprint("events", __name__,
                      template_folder="templates/events")

@blueprint.route("/<event_name>/")
def display_event (event_name):
    # We might need to do more, but that can wait until specifics are known
    return render_template(f"{event_name}.html",
              # TODO this relative path might not work correctly
               event=load_json(f"data/events/{event_name}.json"))

@blueprint.route("/<event_name>/register", methods=("GET", "POST"))
def register_for_event (event_name):
    if request.method == "GET":
        return render_template(f"registration_{event_name}.html")
    if request.method == "POST":
        details = { "participant1_name" : request.form['participant1'],
                    "praticipant2_name" : request.form['participant2'],
                    "team_name" : request.form['team'],
                    "participant1_class" : request.form['clsp1'],
                    "participant2_class" : request.form['clsp2'],
                    "participant1_school" : request.form['school1'],
                    "participant2_school" : request.form['school2'],
                    "praticipant1_email" : request.form['emailp1'],
                    "praticipant2_email" : request.form['emailp2'],
                    "praticipant1_phone" : request.form['mobile1'],
                    "praticipant2_phone" : request.form['mobile2']
                    }
        # Inserting things into the database
        myclient = pymongo.MongoClient("mongodb://pravega.org:27017/")
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

        flash("Email of participant 1 already registered")
        return render_template(f"registration_{event_name}.html")
