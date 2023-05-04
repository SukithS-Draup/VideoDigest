from flask import Flask, request, redirect, url_for, render_template, session
from database.db import *
from database.db import get_data
import subprocess
from runfile import run_python_script


app = Flask(__name__)
app.secret_key = 'abyacb65a6g8scy9a8s'

initialize_db()  # initialize the database


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/main')
def main():
    name = session['username']
    proj=get_data(name)
    return render_template('main.html',username=name,project=proj)

@app.route('/operations')
def operations():
    return render_template('operations.html',username=session['username'])

# initialising logic for each page

@app.route('/login', methods=['POST'])
def submit_login():
    user = request.form['username']
    password = request.form['password']
    resp = validate_user(user, password)
    if resp:
        session['username']=user
        return redirect(url_for('main', username=session['username']))
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

@app.route('/main', methods=['POST'])
def submit_main():
    return redirect(url_for('operations'))

@app.route('/logout')
def handle_form_submission():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/run-stitch')
def run_stitch():
    process = subprocess.Popen(['python', 'C:/Users/Sukith/Desktop/Final year project/VideoDigest/stitch.py'], stdout=subprocess.PIPE)
    output, error = process.communicate()
    return "done"

@app.route('/run-out')
def run_out():
    process = subprocess.Popen(['python', 'C:/Users/Sukith/Desktop/Final year project/VideoDigest/out.py'], stdout=subprocess.PIPE)
    output, error = process.communicate()
    return "done"

if __name__ == '__main__':    app.run(debug=True)
