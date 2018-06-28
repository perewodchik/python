from flask import *
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
	name = StringField('What is your name?', validators=[DataRequired()])
	submit = SubmitField('Submit')

@app.route('/')
def testing():
		return render_template('bootstrap.html')


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404




if __name__ == "__main__":
	#manager.run()
	app.run(host='0.0.0.0', port=5010)
