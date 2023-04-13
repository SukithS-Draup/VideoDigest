from flask import Flask, request, redirect, url_for, render_template
from database.db import *
from pymongo import MongoClient

app = Flask(__name__)

initialize_db()  # initialize the database


# initialising routes for each page

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/main')
def main():
    name = request.args.get('username') 
    return render_template('main.html',username=name)

@app.route('/operations')
def operations():
    return render_template('operations.html')

# initialising logic for each page

@app.route('/login', methods=['POST'])
def submit_login():
    user = request.form['username']
    password = request.form['password']
    resp = validate_user(user, password)
    if resp:
        return redirect(url_for('main', username=user))
    else:
        error = 'Invalid email or password'
    return render_template('login.html', error=error)


@app.route('/signup', methods=['POST'])
def submit_signup():
    user = request.form['username']
    password = request.form['password']
    cnf_password = request.form['cnf_password']
    if password == cnf_password:
        resp = register_user(user, password)
        if resp:
            return redirect(url_for('login'))
        else:
            error = 'User already exists'
    else:
        error = 'Password does not match'
    return render_template('signup.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
