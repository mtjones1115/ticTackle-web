from webapp import app
from flask import render_template, flash, redirect, url_for
from webapp.forms import LoginForm

user = {'username' : 'Clarice'}

results = {
    101: {
        'gameday': 'gameday1',
        'team1': {
            'name': 'Tottenham',
            'goals': '4'
        },
        'team2': {
            'name': 'Saints',
            'goals': '1'
        }
        },
    310: {
        'gameday': 'gameday3',
        'team1': {
            'name': 'United',
            'goals': '2'
        },
        'team2': {
            'name': 'Liverpool',
            'goals': '1'
        }
        },
    
    }

@app.context_processor
def inject_user():
    return dict(user=user['username'])

@app.route('/fixture_list')
def fixtures():
    
    return render_template('fixture_list.html', title='Fixtures', results=results)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    
    message = "This is still clearly underconstruction"
    matches=fixtures()
    
    return render_template('index.html', title='Home', message=message, results=results)

@app.route('/login', methods=['GET','POST'])
def login():
    
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Log In', form=form)

