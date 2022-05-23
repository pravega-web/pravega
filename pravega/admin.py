from flask import (
        Blueprint, flash, g, redirect, render_template, request, session,
        url_for
        )
from werkzeug.security import check_password_hash, generate_password_hash
import pymongo

bp = Blueprint('admin',__name__)

@bp.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        if request.form['username'] == "FAKE PUBLIC USERNAME":
            if request.form['password'] == "the real password":
                return redirect('admin/panel.html')
        return "why u wrogg\n"
    return render_template('admin/login.html')
