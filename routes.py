from app import app, login_manager, db
from flask import render_template, redirect, url_for
from forms import LoginForm, AddLocationForm, AddSiteForm
from flask_login import login_required, login_user, logout_user, current_user
from models import User
from werkzeug.security import check_password_hash
from travellan_models import Locations, Sites

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard', _external=True))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    locations = Locations.query.all()
    return render_template('dashboard.html', binds=app.config['SQLALCHEMY_BINDS'], locations=locations)

@app.route('/travellan/addlocation', methods=['GET', 'POST'])
@login_required
def addLocation():
    addLocation = AddLocationForm(csrf_enabled=False)
    if addLocation.validate_on_submit():
        location = Locations(title=addLocation.title.data, description=addLocation.description.data)
        db.session.add(location)
        db.session.commit()
        return redirect(url_for('dashboard', external=True))
    return render_template('addlocation.html', binds=app.config['SQLALCHEMY_BINDS'], form=addLocation)

@app.route('/travellan/addattraction', methods=['GET', 'POST'])
@login_required
def addAttraction():
    addSite = AddSiteForm(csrf_enabled=False)
    addSite.location.choices = [(location.id, location.title) for location in Locations.query.all()]
    if addSite.validate_on_submit():
        site = Sites(title=addSite.title.data, description=addSite.description.data, loc_id=addSite.location.data)
        db.session.add(site)
        db.session.commit()
        return redirect(url_for('dashboard', external=True))
    return render_template('addsite.html', binds=app.config['SQLALCHEMY_BINDS'], form=addSite)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login', _external=True))
