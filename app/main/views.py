from . import main
from flask import render_template, abort
from ..models import User
from .. import db


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/post')
def post():
    return render_template('post.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/user/uname')
def profife(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)