from myproject import db,app
from flask import render_template,redirect,flash,abort,url_for,request
from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')