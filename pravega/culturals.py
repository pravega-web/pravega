from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for
        )
blueprint = Blueprint('culturals', __name__, template_folder="templates/culturals")

@blueprint.route("generic/register", methods=("GET", "POST"))
def generic_culturals_register():
    event_name = "eventname"
    if request.method == "GET":
        return render_template("registration/registration_generic.html")
    if request.method == "POST":
        return "yobama"
