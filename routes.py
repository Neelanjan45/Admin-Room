from app import app
from flask import render_template
from forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(csrf_enabled=False)
    return render_template('login.html', form=form)