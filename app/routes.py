from flask import render_template, url_for, flash, redirect, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import UserForm, RegistrationForm, EditProfileForm
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        print(f"User {form.username.data} created with email {form.email.data}")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid Username or Password.")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        # in case redirect(next_page) breaks
        #return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_required
@app.route('/memrec', methods=['GET','POST'])
def memrec():
    if current_user.is_anonymous:
        return redirect(url_for('index'))
    return render_template('memrec.html',title='Member Information.')

@app.route('/tools', methods=['GET'])
def tools():

    websiteData = {
        'Sparrows': 'https://www.sparrowslockpicking.ca',
        'Peterson': 'https://www.thinkpeterson.com',
        'Law Lock Tools': 'https://www.lawlocktools.co.uk',
        'Multipick': 'https://shop.multipick.com/en/index',
        'Southord': 'https://www.southord.com/',
        'Southern Specialties': 'https://lockpicktools.com/',
        'UK Bump Keys': 'https://www.ukbumpkeys.com/collections/lock-pick-sets',
        'Banggood (DANIU Dimple Picks)':'https://www.banggood.com/',
        'Mako Locks': 'https://makolocks.com'
    }
    return render_template('tools.html', title='Tools and Resources.',
     tool_data=websiteData)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user, title='User Home')

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


def save_picture(form_picture):
    basedir = os.path.abspath(os.path.dirname(__file__))
    secrets = "super-secret!"
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = secrets + f_ext
    avatar_account = str(current_user.username)
    picture_path = os.path.join(basedir, url_for(
        'static',
        filename='images/'+avatar_account+'/'),picture_fn)
    #form_picture.save(picture_path)
    return picture_fn

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        if form.avatar.data:
            picture_file = save_picture(form.avatar.data)
            current_user.avatar = picture_file
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        print("Changes saved.")
        return redirect(url_for('user', username=form.username.data))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        print("fail")
    return render_template('edit_profile.html', title='Edit Profile', form=form)