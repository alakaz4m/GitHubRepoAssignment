from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'asdkhk1jh3123fsda'


@app.route('/')
def index():
	if 'nums' not in session:
		session['nums'] = 1
		print session['nums']
	else:
		session['nums'] = session['nums'] + 1
	return render_template('index.html')

@app.route('/process/<status>', methods=['POST']) #figure out how to make this run with reset and +2 counter instead of a seperate form and route
def process(status):
	if status == 'count':
		session['nums'] = session['nums'] + 1
		return redirect('/')
	else:
		session['nums'] = 0
		return redirect('/')

#@app.route('/process/reset', methods=['POST'])
#def reset():
#	session['nums'] = 0
#	return redirect('/')

app.run(debug=True)