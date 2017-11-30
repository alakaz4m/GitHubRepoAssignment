import random
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'mySecret'

@app.route('/', methods=['GET', 'POST'])
def index():
	winner = 'inline'
	playornot = 'Submit'
	color_box = '#FFFFFF'
	outcome = ''
	outcomeshow = 'none'
	
	if 'value' not in session:
		outcomeshow = 'none'
		session['value'] = random.randint(1,101)
		return redirect('/')
	else:
		print session['value']
		
	if 'guessNum' in request.form:
		if len(request.form['guessNum']) == 0:
			   return redirect('/')
		if int(request.form['guessNum']) == session['value']:
			outcomeshow = 'block'
			outcome = 'You win! Good job!'
			color_box = "#00BE79"
			winner = 'none'
			playornot = 'Play Again!'
			session.pop('value')
		elif int(request.form['guessNum']) > session['value']:
			outcomeshow = 'block'
			outcome = 'You lost. Too high!'
			color_box = "#FF4949"
		elif int(request.form['guessNum']) < session['value']:
			outcomeshow = 'block'
			outcome = 'You lost. Too low!'
			color_box = "#FF4949"
	return render_template('index.html', outcome=outcome, color_box=color_box, playornot=playornot, winner=winner, outcomeshow=outcomeshow)

app.run(debug=True)