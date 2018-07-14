from flask import *
from flask_session import Session
from caesar import caesar_cipher
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime, date


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine("postgres://ucurzlfkjmcwqf:0ef9496e10a6f8fd80f6af62bc2c7b200a7f1e6b08f20ba815d9bbc9be550518@ec2-54-227-240-7.compute-1.amazonaws.com:5432/dct3cpbvs21gfs")
db = scoped_session(sessionmaker(bind=engine))


@app.route('/', methods=["GET", "POST"])
def index():


	if request.form.get("btn_logout") == "logout":
		session["logged_in"] = False
		session["username"] = ""

	name = "anonymous"
	greetings_message = "Hi there, kind stranger"
	if session["logged_in"]:
		greetings_message = f"{session['username']}, you are logged in. POGGERS MY DOGGERS"
		name = session["username"]


	note = request.form.get("note")
	if note != "" and note != None:
		db.execute(
				"INSERT INTO notes (username, note) VALUES (:username, :note)",
	            {"username": name,  "note": note}
		)
		db.commit()

	notes = db.execute("SELECT * FROM NOTES").fetchall()
	return render_template("index.html", notes=notes, greetings_message=greetings_message)



@app.route('/login', methods=['GET', "POST"])
def login():
	if request.method == "POST":
		name = request.form.get("log_name")
		password = request.form.get("log_pass")
		user_row = db.execute("SELECT * FROM user_info WHERE username = :username", {"username": name})
		if user_row.rowcount == 0:
			error_message = "The credentials you have provided are invalid"
			return render_template("error.html", error_message=error_message)

		elif user_row.fetchone().password == password:
				session["logged_in"] = True
				session["username"] = name
		else:
			error_message = "The credentials you have provided are invalid"
			return render_template("error.html", error_message=error_message)

		return redirect( url_for('index') )
	return render_template("login.html")


@app.route('/registration_success', methods=["POST"])
def registration_success():
	today = date.today().timetuple()
	name = request.form.get("reg_name")
	password = request.form.get("reg_pass")

	if db.execute("SELECT * FROM user_info WHERE username = :username", {"username": name}).rowcount == 0:
		db.execute(
				"INSERT INTO user_info (username, password, register_date) VALUES (:username, :password, :register_date )",
	            {"username": name, "password": password, "register_date": f"{today[0]}-{today[1]}-{today[2]}" }
		)
		db.commit()
		session["logged_in"] = True
		session["username"] = name
	else:
		error_message = "Someone already registered with that name"
		return render_template("error.html", error_message=error_message)
	return redirect( url_for('index') )


@app.route("/caesar", methods=["GET", "POST"])
def caesar():
	if request.method == "POST":
		string = request.form.get("caesar_text")
		shift = int( request.form.get("caesar_key") )
		print("string", string, "shift",shift)
		encrypted_string = caesar_cipher(string, shift)
		print("encrypted_string", encrypted_string)
		return render_template("caesar.html", string=string, shift=shift, encrypted_string=encrypted_string)

	return render_template("caesar.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0')
