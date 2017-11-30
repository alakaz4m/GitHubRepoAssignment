from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['myname']
	print name
	return render_template('process.html', myname=name)

app.run(debug=True)
