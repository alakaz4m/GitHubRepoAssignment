from flask import Flask, render_template, request, redirect, flash
import re

app = Flask(__name__)
app.secret_key = "loasdadajasd23"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['email']) < 1:
		flash("Error, email length")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Error, emal not valid")
	else:
		flash('Success!')
	return redirect('/')

app.run(debug=True)