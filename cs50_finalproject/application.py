import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology

lista = [0]
# Configure application - Copied from Problem set 8
app = Flask(__name__)

# Ensure templates are auto-reloaded - Copied from Problem set 8
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies) - Copied from problem set 8
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Ensure responses aren't cached - Copied from Problem set 8


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies) - Copied from Problem set 8
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///appeople.db")

# Register - Copied from Problem set 8
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Render register page
    if request.method == "GET":
        print("0")
        return render_template("register.html")

    # Checking if user provided all the required fields correctly and if the username is taken
    elif request.method == "POST":
        print("teste 1")
        if not request.form.get("username"):
            print("teste 2")
            return apology ("You must provide a username.")
            print("0")
        print("1")

        if not request.form.get("email"):
            return apology ("You must provide a valid email.")
        print("2")
        if not request.form.get("password"):
            return apology ("You must provide a password.")

        if not request.form.get("confirmation"):
            return  apology("You must confirm your password.")

        if request.form.get("password") != request.form.get("confirmation"):
            return apology ("Your passwords don't match! Try typing again.")

        if not db.execute("SELECT username FROM users WHERE username = :username", username=request.form.get("username")):
            hashword = generate_password_hash(request.form.get("password"))
            users = db.execute("INSERT INTO users (username, hashword) VALUES(:username, :hash)",
                               username=request.form.get("username"), hash=hashword)
            rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
            session["user_id"] = rows[0]["user_id"]
            return redirect("/index")

        elif True:
            return apology ("Username was already taken!")

@app.route("/", methods=["GET"])
def blog():
    return render_template("blog.html")

@app.route("/personality", methods=["GET", "POST"])
@login_required
def personality():
    if request.method == "GET":
        print(0)
        return render_template("personality.html")
        session["user_id"]

    if request.method == "POST":
        #extraversion = int(request.form.get("EXT1")) + int(request.form.get("EXT3")) + int(request.form.get("EXT5")) +  int(request.form.get("EXT7")) +  int(request.form.get("EXT9")) - int(request.form.get("EXT2")) -  int(request.form.get("EXT4")) -  int(request.form.get("EXT6")) -  int(request.form.get("EXT8")) - int(request.form.get("EXT10"))
        extraversion = int(request.form.get("EXT1")) + int(request.form.get("EXT3")) + int(request.form.get("EXT5")) +  int(request.form.get("EXT7")) + int(request.form.get("EXT9")) - int(request.form.get("EXT2")) - int(request.form.get("EXT4")) - int(request.form.get("EXT6")) - int(request.form.get("EXT8")) - int(request.form.get("EXT10"))
        agreeableness = int(request.form.get("AGR2")) + int(request.form.get("AGR4")) + int(request.form.get("AGR6")) +  int(request.form.get("AGR8")) +  int(request.form.get("AGR9")) + int(request.form.get("AGR10")) - int(request.form.get("AGR1")) -  int(request.form.get("AGR3")) - int(request.form.get("AGR5")) - int(request.form.get("AGR7"))
        consciousness = int(request.form.get("CSN1")) + int(request.form.get("CSN3")) + int(request.form.get("CSN5")) +  int(request.form.get("CSN7")) +  int(request.form.get("CSN9")) + int(request.form.get("CSN10")) - int(request.form.get("CSN2")) -  int(request.form.get("CSN4")) - int(request.form.get("CSN6")) - int(request.form.get("CSN8"))
        estability = int(request.form.get("EST2")) + int(request.form.get("EST4")) - int(request.form.get("EST1")) - int(request.form.get("EST3")) - int(request.form.get("EST5")) - int(request.form.get("EST6")) - int(request.form.get("EST7")) - int(request.form.get("EST8")) - int(request.form.get("EST9")) - int(request.form.get("EST10"))
        openess = int(request.form.get("OPN1")) + int(request.form.get("OPN3")) + int(request.form.get("OPN5")) + int(request.form.get("OPN7")) +  int(request.form.get("OPN8")) + int(request.form.get("OPN9")) + int(request.form.get("OPN10")) - int(request.form.get("OPN2")) - int(request.form.get("OPN4")) -  int(request.form.get("OPN6"))

        db.execute("INSERT INTO traits (EXT, AGR, CON, EST, OPN, user_id) VALUES (:EXT, :AGR, :CON, :EST, :OPN, :user_id)",
        EXT=extraversion, AGR=agreeableness, CON=consciousness, EST=estability, OPN=openess, user_id=session["user_id"])
    return apology("deu certo sim")


#@app.route("/personality_results", methods=["GET"])
#@login_required
#def personality_results():
#    if request.method == "GET":
#        return render_template("personality_results.html")

@app.route("/lifestyle", methods=["GET", "POST"])
@login_required
def lifestyle():
    if request.method == "GET":
        return render_template("lifestyle.html")
        session["user_id"]

    if request.method == "POST":
        db.execute("INSERT INTO traits (lf1, lf2, lf3, lf4, lf5, lf6, lf7, lf8, lf9, lf10, lf11, lf12, lf13, lf14, lf15) VALUES (:lf1, :lf2, :lf3, :lf4, :lf5, :lf6, :lf7, :lf8, :lf9, :lf10, :lf11, :lf12, :lf13, :lf14, :lf15",
        lf1=request.form.get("lf1"), lf2=request.form.get("lf2"), lf3=request.form.get("lf3"), lf4=request.form.get("lf4"), lf5=request.form.get("lf5"), lf6=request.form.get("lf6"), lf7=request.form.get("lf7"), lf8=request.form.get("lf8"), lf9=request.form.get("lf9"), lf10=request.form.get("lf10"), lf11=request.form.get("lf11"), lf12=request.form.get("lf12"), lf13=request.form.get("lf13"), lf14=request.form.get("lf14"), lf15=request.form.get("lf15"))

@app.route("/index", methods=["GET", "POST"])
@login_required
def index():
    return render_template("index.html")



@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format. Copied from Problem Set 8"""
    username = request.args.get("username")
    rows = db.execute("SELECT * FROM users WHERE username = :username", username=username)

    # If inputed username does not have at least 1 character and is not taken
    if len(username) > 1 and not rows:
        return jsonify(True)

    else:
        return jsonify(False)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hashword"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["user_id"]

        # Redirect user to home page
        return redirect("/index")


@app.route("/interests", methods=["GET", "POST"])
@login_required
def match():
    if request.method == "GET":
        return render_template("interests.html")
    #user = db.execute("SELECT * FROM students WHERE user_id = :user_id", user_id=session["user_id"])
    if request.method == "POST":
        user = db.execute("SELECT * FROM users WHERE user_id = :user_id", user_id=1)
        print(user)
        attributes = db.execute("SELECT * FROM students")

        #environment = db.execute("SELECT * FROM students WHERE environment = :environment AND year = :year AND country = :country AND color = :color AND house = :house",
        #environment=attributes[0]['environment'], year=attributes[0]['year'], country=attributes[0]['country'], color=user_color = attributes[0]['color'], house=user_house = attributes[0]['house'])
        #print(environment)
