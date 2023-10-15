# import git
from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = '79f11d1e73573998f815b165868cd307'

@app.route("/")
def home():
    return render_template('home.html', subtitle = "Home Page")

@app.route("/login/")
def login():
    return render_template('login.html', subtitle = "Login Page")

@app.route("/dashboard/")
def dashboard():
    return render_template('dashboard.html', subtitle = "Dashboard Page")

@app.route("/update_server/", methods=['POST'])
def webhook():
    if request.method == "POST":
        repo = git.Repo('/home/pennypal/pennypal')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere Successfully', 200
    else: 
        return 'Wrong event type', 400





