from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'asdasdhb2hb31j23hbq'

@app.route('/')
def rootpage():
	if 'red' in session and 'green' in session and 'blue' in session:
		red = session['red']
		green = session['green']
		blue = session['blue']
	else:
		red = 0
		green = 0
		blue = 0
	return render_template('index.html', red=red, green=green, blue=blue)


@app.route('/process', methods = ['POST'])
def process():
	session['red'] = request.form['red']
	session['green'] = request.form['green']
	session['blue'] = request.form['blue']
	return redirect('/')
app.run(debug=True)