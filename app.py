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

        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in Successfully!")

            next = request.args.get('next')

            if next is None or next[0] != '/':
                next = url_for('welcome_user')

            return redirect(next)
        
        flash("Login Unsuccessful. Please check email and password.")
        return render_template('login.html', form=form)

    return render_template('login.html', form=form)

    
@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user:
            flash('Email already registered!')
            return redirect(url_for('register'))
        
        new_user = User(email=form.email.data, username=form.username.data, password=form.password.data)

        db.session.add(new_user)
        db.session.commit()
        flash('Thanks for registration!')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)


