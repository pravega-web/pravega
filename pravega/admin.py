import functools
from flask import (
        Blueprint, flash, g, redirect, render_template, request, session,
        url_for
        )
from werkzeug.security import check_password_hash, generate_password_hash
import pymongo

bp = Blueprint('admin',__name__,template_folder='/admin')

admin_username = 'lmao'
admin_password = 'lmao'

my_mng = pymongo.MongoClient("mongodb://localhost:27017")
my_db = my_mng["registrations"]
my_col = my_db["event"]

loli=my_col.find_one()
headings=tuple(loli.keys())
data=[]
for lol in my_col.find():
    data.append(tuple([lol[head] for head in headings]))
data=tuple(data)

"""headings = ("a", "b", "c")
data = (
    (1,2,3),
    (4,5,6)
)
"""
@bp.route('/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        if request.form['username'] == admin_username:
            if request.form['password'] == admin_password:
                session.clear()
                session['user_id'] = "42069"
                return redirect(url_for('admin.panel'))
        return "why u wrogg\n"
    return render_template('admin/login.html')

@bp.before_app_request
def load_logged_in_admin():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    if user_id == "42069":
        g.user = user_id


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('admin.login'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('admin.login'))
        elif session.get('user_id') != "42069" :
            return redirect(url_for('admin.login'))

        return view(**kwargs)
    return wrapped_view
#
#
# CALL AND IMPLEMENT THE MONGODB FUNCTIONS
#
#

@bp.route('/panel', methods=('GET','POST'))
@login_required
def panel():
    if request.method == 'GET':
        return render_template("admin/panel.html", headings=headings, data=data)
