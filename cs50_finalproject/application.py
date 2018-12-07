import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
import sys
from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter
from timeit import timeit
import smtplib

from helpers import login_required, apology

lista = [0]
server = smtplib.SMTP('smtp.gmail.com', 587)

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
            users = db.execute("INSERT INTO users (username, hashword, email) VALUES(:username, :hash, :email)",
                               username=request.form.get("username"), hash=hashword, email=request.form.get("email"))
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

        user = db.execute("SELECT user_id FROM traits where user_id = :user_id", user_id=session["user_id"])
        if not user:
            db.execute("INSERT INTO traits (EXT, AGR, CON, EST, OPN, user_id) VALUES (:EXT, :AGR, :CON, :EST, :OPN, :user_id)",
                        EXT=extraversion, AGR=agreeableness, CON=consciousness, EST=estability, OPN=openess, user_id=session["user_id"])
            return redirect("/interests")
        else:
            db.execute("UPDATE traits SET EXT=:EXT, AGR=:AGR, CON=:CON, EST=:EST, OPN=:OPN WHERE user_id= :user_id",
            EXT=extraversion, AGR=agreeableness, CON=consciousness, EST=estability, OPN=openess, user_id=session["user_id"])
            return redirect("/interests")


    return redirect("/interests")


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
        if request.form.get("lf1"):
            lf1 = 1
        else:
            lf1 = 0

        if request.form.get("lf2"):
            lf2 = 1
        else:
            lf2 = 0

        if request.form.get("lf3"):
            lf3 = 1
        else:
            lf3 = 0

        if request.form.get("lf4"):
            lf4 = 1
        else:
            lf4 = 0

        if request.form.get("lf5"):
            lf5 = 1
        else:
            lf5 = 0

        if request.form.get("lf6"):
            lf6 = 1
        else:
            lf6 = 0

        if request.form.get("lf7"):
            lf7 = 1
        else:
            lf7 = 0

        if request.form.get("lf8"):
            lf8 = 1
        else:
            lf8 = 0

        if request.form.get("lf9"):
            lf9 = 1
        else:
            lf9 = 0

        if request.form.get("lf10"):
            lf10 = 1
        else:
            lf10 = 0

        if request.form.get("lf11"):
            lf11 = 1
        else:
            lf11 = 0

        if request.form.get("lf12"):
            lf12 = 1
        else:
            lf12 = 0

        if request.form.get("lf13"):
            lf13 = 1
        else:
            lf13 = 0

        if request.form.get("lf14"):
            lf14 = 1
        else:
            lf14 = 0

        if request.form.get("lf15"):
            lf15 = 1
        else:
            lf15 = 0

        user = db.execute("SELECT user_id FROM traits where user_id = :user_id", user_id=session["user_id"])
        if not user:
            db.execute("INSERT INTO traits (lf1, lf2, lf3, lf4, lf5, lf6, lf7, lf8, lf9, lf10, lf11, lf12, lf13, lf14, lf15, user_id) VALUES (:lf1, :lf2, :lf3, :lf4, :lf5, :lf6, :lf7, :lf8, :lf9, :lf10, :lf11, :lf12, :lf13, :lf14, :lf15, :user_id)",
            lf1=lf1, lf2=lf2, lf3=lf3, lf4=lf4, lf5=lf5, lf6=lf6, lf7=lf7, lf8=lf8, lf9=lf9, lf10=lf10, lf11=lf11, lf12=lf12, lf13=lf13, lf14=lf14, lf15=lf15, user_id=session["user_id"])
            return redirect("/interests")
        else:
            db.execute("UPDATE traits SET lf1=:lf1, lf2=:lf2, lf3=:lf3, lf4=:lf4, lf5=:lf5, lf6=:lf6, lf7=:lf7, lf8=:lf8, lf9=:lf9, lf10=:lf10, lf11=:lf11, lf12=:lf12, lf13=:lf13, lf14=:lf14, lf15=:lf15 WHERE user_id= :user_id",
            lf1=lf1, lf2=lf2, lf3=lf3, lf4=lf4, lf5=lf5, lf6=lf6, lf7=lf7, lf8=lf8, lf9=lf9, lf10=lf10, lf11=lf11, lf12=lf12, lf13=lf13, lf14=lf14, lf15=lf15, user_id=session["user_id"])
            return redirect("/interests")

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

@app.route("/match", methods=["GET", "POST"])
@login_required
def match():

    if request.method == "GET":
        openess = db.execute("SELECT OPN FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['OPN']
        agreeableness = db.execute("SELECT AGR FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['AGR']
        estability = db.execute("SELECT EST FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['EST']
        consciousness = db.execute("SELECT CON FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['CON']
        extraversion = db.execute("SELECT EXT FROM traits WHERE user_id=:user_id", user_id=session["user_id"])[0]['EXT']

        opn = db.execute("SELECT user_id FROM traits WHERE OPN BETWEEN :value1 AND :value2", value1=openess-5, value2=openess+5)
        agr = db.execute("SELECT user_id FROM traits WHERE AGR BETWEEN :value1 AND :value2", value1=agreeableness-5, value2=agreeableness+5)
        est = db.execute("SELECT user_id FROM traits WHERE EST BETWEEN :value1 AND :value2", value1=estability-5, value2=estability+5)
        con = db.execute("SELECT user_id FROM traits WHERE CON BETWEEN :value1 AND :value2", value1=consciousness-5, value2=consciousness+5)
        ext = db.execute("SELECT user_id FROM traits WHERE EXT BETWEEN :value1 AND :value2", value1=extraversion-5, value2=extraversion+5)

        for item in opn:
            lista.append(item['user_id'])
        for item in agr:
            lista.append(item['user_id'])
        for item in est:
            lista.append(item['user_id'])
        for item in con:
            lista.append(item['user_id'])
        for item in ext:
            lista.append(item['user_id'])

        lf1 = db.execute("SELECT lf1 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf1']
        lf2 = db.execute("SELECT lf2 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf2']
        lf3 = db.execute("SELECT lf3 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf3']
        lf4 = db.execute("SELECT lf4 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf4']
        lf5 = db.execute("SELECT lf5 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf5']
        lf6 = db.execute("SELECT lf6 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf6']
        lf7 = db.execute("SELECT lf7 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf7']
        lf8 = db.execute("SELECT lf8 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf8']
        lf9 = db.execute("SELECT lf9 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf9']
        lf10 = db.execute("SELECT lf10 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf10']
        lf11 = db.execute("SELECT lf11 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf11']
        lf12 = db.execute("SELECT lf12 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf12']
        lf13 = db.execute("SELECT lf13 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf13']
        lf14 = db.execute("SELECT lf14 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf14']
        lf15 = db.execute("SELECT lf15 FROM traits WHERE user_id=:user_id",user_id=session["user_id"])[0]['lf15']

        lifestyle1 = db.execute("SELECT user_id FROM traits WHERE lf1=:lf1", lf1=lf1)
        lifestyle2 = db.execute("SELECT user_id FROM traits WHERE lf2=:lf2", lf2=lf2)
        lifestyle3 = db.execute("SELECT user_id FROM traits WHERE lf3=:lf3", lf3=lf3)
        lifestyle4 = db.execute("SELECT user_id FROM traits WHERE lf4=:lf4", lf4=lf4)
        lifestyle5 = db.execute("SELECT user_id FROM traits WHERE lf5=:lf5", lf5=lf5)
        lifestyle6 = db.execute("SELECT user_id FROM traits WHERE lf6=:lf6", lf6=lf6)
        lifestyle7 = db.execute("SELECT user_id FROM traits WHERE lf7=:lf7", lf7=lf7)
        lifestyle8 = db.execute("SELECT user_id FROM traits WHERE lf8=:lf8", lf8=lf8)
        lifestyle9 = db.execute("SELECT user_id FROM traits WHERE lf9=:lf9", lf9=lf9)
        lifestyle10 = db.execute("SELECT user_id FROM traits WHERE lf10=:lf10", lf10=lf10)
        lifestyle11 = db.execute("SELECT user_id FROM traits WHERE lf11=:lf11", lf11=lf11)
        lifestyle12 = db.execute("SELECT user_id FROM traits WHERE lf12=:lf12", lf12=lf12)
        lifestyle13 = db.execute("SELECT user_id FROM traits WHERE lf13=:lf13", lf13=lf13)
        lifestyle14 = db.execute("SELECT user_id FROM traits WHERE lf14=:lf14", lf14=lf14)
        lifestyle15 = db.execute("SELECT user_id FROM traits WHERE lf15=:lf15", lf15=lf15)

        for item in lifestyle1:
            lista.append(item['user_id'])
        for item in lifestyle2:
            lista.append(item['user_id'])
        for item in lifestyle3:
            lista.append(item['user_id'])
        for item in lifestyle4:
            lista.append(item['user_id'])
        for item in lifestyle5:
            lista.append(item['user_id'])
        for item in lifestyle6:
            lista.append(item['user_id'])
        for item in lifestyle7:
            lista.append(item['user_id'])
        for item in lifestyle8:
            lista.append(item['user_id'])
        for item in lifestyle9:
            lista.append(item['user_id'])
        for item in lifestyle10:
            lista.append(item['user_id'])
        for item in lifestyle11:
            lista.append(item['user_id'])
        for item in lifestyle12:
            lista.append(item['user_id'])
        for item in lifestyle13:
            lista.append(item['user_id'])
        for item in lifestyle14:
            lista.append(item['user_id'])
        for item in lifestyle15:
            lista.append(item['user_id'])

        #Calculating which user appears the most number of times
        user_id=session["user_id"]
        #list(filter(lambda a: a != user_id, lista))
        print(lista)
        nova = [x for x in lista if x != user_id]
        print(nova)
        partner = max(set(nova), key=nova.count)
        print(partner)
        name = db.execute("SELECT username, email FROM users WHERE user_id=:user_id", user_id=partner)

        print(name)

        return render_template("personality_results.html", name=name)

    #if request.method == "POST":
     #   return render_template("personality_results.html", name=name)

@app.route("/interests", methods=["GET", "POST"])
@login_required
def interests():
    if request.method == "GET":
        return render_template("interests.html")

@app.route("/logout")
def logout():
    """Log user out - Copied from Problem set 8"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")