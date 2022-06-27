"""Implements event webpages including registration.

Variable `blueprint`: a `flask.Blueprint` for the event pages and event
registration pages."""

# Assumptions about how to find external data (can be changed as needed):
# + For each event accessible at URL "/events/<event_name>":
#   + file templates/events/<event_name>.html: Jinja template for that page
#   + file data/events/<event_name>.json: JSON file, available in the Jinja
#     template as variable `event`

from json import load as load_json
from json import dumps
from flask import Blueprint, render_template,request, flash, redirect, url_for
import pymongo
import razorpay

blueprint = Blueprint("events", __name__,
                      template_folder="templates/events")

@blueprint.route("/<event_name>/")
def display_event (event_name):
    # We might need to do more, but that can wait until specifics are known
    return render_template(f"{event_name}.html",
              # TODO this relative path might not work correctly
               event=load_json(f"data/events/{event_name}.json"))
