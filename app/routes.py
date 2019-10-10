from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'slsh'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Nice day in Kyiv!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Joker is so wonderful movie!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
