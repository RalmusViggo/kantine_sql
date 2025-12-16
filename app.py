from flask import Flask, render_template, redirect, session
import mysql.connector
from forms import RegisterForm, LoginForm
import random
import datetime
from datetime import date

app = Flask(__name__)
app.secret_key = "hemmelig-nok"

# Enkel DB-tilkobling
def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="rasmus",
        password="R-asmus150508",
        database="test"
    )

@app.route('/')
def index():
    beple = {"class": "eple", "bildekilde": "/static/images/pixel_art_large.png"}
    return render_template("index.html", beple = beple)

# Registrering
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        navn = form.name.data
        brukernavn = form.username.data
        passord = form.password.data
        adresse = form.address.data

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO brukere (navn, brukernavn, passord, adresse) VALUES (%s, %s, %s, %s)",
            (navn, brukernavn, passord, adresse)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect("/login")

    return render_template("register.html", form=form)

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        brukernavn = form.username.data
        passord = form.password.data

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT navn FROM brukere WHERE brukernavn=%s AND passord=%s",
            (brukernavn, passord)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            session['navn'] = user[0]  # lagrer navnet i session
            return redirect("/welcome")
        else:
            form.username.errors.append("Feil brukernavn eller passord")

    return render_template("login.html", form=form)

# Velkomstside
@app.route("/welcome")
def welcome():
    navn = session.get('navn')  # Hent navn fra session
    if not navn:
        return redirect("/login")  # send tilbake til login om ikke logget inn
    return render_template("welcome.html", name=navn)

@app.route('/meny.html')
def meny():
    day = date.today()
    dag = {
        "Monday" : {
            "knekkebrød", "brød", "leverpostei", "kaviar", "ost"
            },
        "Tuesday" : {
            "knekkebrød", "brød", "jordbær syltetøy", "bringebær syltetøy", "skinke"
            },
        "Wednesday" : {
            "knekkebrød", "brød", "salami", "brunost", "ost"
            },
        "Thursday" : {
            "knekkebrød", "brød", "smør", "skinke", "kaviar"
            },
        "Friday" : {
            "knekkebrød", "brød", "kaviar", "makrellitomat", "sursild"
            }
        },
    varmmat = {
            "Monday" : {
                "kokte wienerpølser"
                },
            "Tuesday" : {
                "en tallerken med kokte poteter."
                },
            "Wednesday" : {
                "en tallerken med kokt brokkoli."
                },
            "Thursday" : {
                "en skål med varm havregrøt."
                },
            "Friday" : {
                "laktose-fri pizza med pepperoni."
                }
            }
    return render_template("meny.html", day=day, dag=dag, varmmat=varmmat)

@app.route('/varer.html')
def varer():
    return render_template("varer.html")

@app.route('/kontakt.html')
def kontakt():
    return render_template("kontakt.html")

if __name__ == "__main__":
    app.run(host='172.20.128.25' , port=46621, debug=True)
    
    







"""vare = {
    "sjokomelk": {
        "pris: ": "100"
    },
    "yoghurt": {
        "vanilje": {"pris: ": 100}, 
        "jordbær": {"pris: ": 100},
        "skogsbær": {"pris: ": 100}
    },
    "brus": {
        "cola zero": {"pris: " : 100},
        "cola": {"pris: " : 100},
        "sprite": {"pris: " : 100},
        "fanta": {"pris: " : 100}
    }
}"""