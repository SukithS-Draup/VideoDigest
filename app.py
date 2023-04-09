from flask import Flask, request, redirect, url_for, render_template
from database.db import *
from pymongo import MongoClient
import atexit

app = Flask(__name__)

initialize_db()
atexit.register(db_exit)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/', methods=['POST'])
def submit_login():
    try:
        users = client['videodigest']['users']
    except:
        return "user not found"
    login_user = users.find_one({'name': request.form['username']})
    if login_user:
        if request.form['password'] == login_user['password']:
            return redirect(url_for('main'))
    return 'Invalid username/password combination'


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def submit_signup():
    if request.method == 'POST':
        users = client['videodigest']['users']
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            users.insert({'name': request.form['username'], 'password': request.form['password']})
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('signup.html')


@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
