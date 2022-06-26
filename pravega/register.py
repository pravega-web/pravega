from flask import (
        Blueprint, flash, g, redirect, render_template, request, url_for
        )
from werkzeug.exceptions import abort

from pravega.db import get_db

bp = Blueprint('register',__name__)

@bp.route('/chemenigma' methods=('GET', 'POST'))
def register_chemenigma(eventname):
    if request.method == 'POST':
        variable = request.form['variable']

        if all correct:
            db = get_db()
            existing_user = users.find_one({'mobile' : request.form['mobile']})

            if existing_user is None:
                users.insert_one(
                        {   'mobile' : request.form['mobile'],
                            'teamname' : request.form['teamname'],
                            'password' : hashpass,
                            'participant1' : request.form['participant1'],
                            'class1' : request.form['class1'],
                            'participant2' : request.form['participant2'],
                            'class2' : request.form['class2'],
                            'email': request.form['email'],
                            'school' : request.form['school'],
                            'schooladdress' : request.form['schooladdress'],
                            'prelims1':'NA',
                            'prelims2':'NA',
                            'referralregwith':'','personalref':"" })
                session['mobile'] = request.form['mobile']
                return redirect(url_for('index'))

            flash('This mobile number is already registered. Please log in to continue.')



            close db
            return redirect(url_for('something'))
    return render_template('registration_chemenigma.html')
