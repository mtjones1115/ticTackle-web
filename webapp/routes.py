from webapp import app
from flask import render_template


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
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
    return render_template('index.html', title='Home', user=user, results=results)