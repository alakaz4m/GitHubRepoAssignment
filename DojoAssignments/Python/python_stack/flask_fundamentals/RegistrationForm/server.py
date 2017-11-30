from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "ahsdashdkh2jeh2j389asd"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
	for key in request.form:
		for value in request.form:
			if len(value) < 1:
				flash("All fields must be filled")
				return redirect('/')