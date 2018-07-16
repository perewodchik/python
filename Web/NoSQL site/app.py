from flask import *
from flask_session import Session
from caesar import caesar_cipher
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime, date
from vk_api import User

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/', methods=["GET", "POST"])
def index():
	return render_template("index.html")


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

@app.route("/vk", methods=["GET", "POST"])
def vk():
	string_info = ["-"]
	popushennost = ["-"]
	if request.method == "POST":
		id = int(request.form.get("user_id"))
		user = User(id)
		print(user)
		string_info = user.user_info()
		print(user.user_info())
		popushennost = user.popushennost_test()
	return render_template("vk.html", string_info=string_info, popushennost=popushennost)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
