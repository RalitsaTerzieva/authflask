from myproject import db,app
from flask import render_template,redirect,flash,abort,url_for,request
from flask_login import login_user,login_required,logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out!')
    return redirect(url_for('home'))

@app.route('/login', methods=["POST", "GET"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Logged in Successfully!")

            next = request.args.get('next')

            if next is not None or not next[0] == '/':
                next = url_for('welcome_user')

            return redirect(next)
        
        return render_template('login.html', form=form)

