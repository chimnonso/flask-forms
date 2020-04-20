from flask import Flask, render_template, redirect, url_for
from flask_bootstrap  import Bootstrap
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, TextField, DateField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = "some keys"



class MyForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    dept = StringField('Department', validators=[DataRequired()])
    feedback = TextField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Submit')
    

@app.route('/', methods=('GET', 'POST'))
def index():
    form = MyForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('index.html', form=form)

@app.route('/success')
def success():
   return render_template('success.html')


if __name__ == "__main__":
    app.run(debug=True)
