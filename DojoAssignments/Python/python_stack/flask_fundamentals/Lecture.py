from flask import Flask, render_template, sesson, redirect
app = Flask(__name__)

app.secret_key = 'ajkhaia89sdyah2dhkj2haksd987'

@app.route('/')
def index():
	if 'user' in session:
		name = session['name']
		email = session['email']
	else:
		name = False
		email = False
		email = False
		status = 'Not Logged in'
	return render_template('index.html', template_status = status)
@app.route('/login')
def login():
	session['name'] = request.form['name']
	session['email'] = request.form['email']
	return redirect('/')

@app.route('/logout')
def logout():
	session.pop('user')
	return redirect('/')

app.run(debug=True)