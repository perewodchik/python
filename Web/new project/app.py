from flask import *

app = Flask(__name__)

@app.route('/')
def testing():
		print( url_for('static', filename='bootstrap.css') )
		return render_template("bootstrap.html")

if __name__ == "__main__":
	app.run(host='0.0.0.0')
