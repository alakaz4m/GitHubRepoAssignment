from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def nope():
	return render_template('index.html')

@app.route('/ninja')
def squad():
	return render_template('ninjas.html')

@app.route('/ninja/<color>')
def single_ninja(color):
	if color == "blue":
		color_str = "leonardo.jpg"
	elif color == "orange":
		color_str = "michelangelo.jpg"
	elif color == "purple":
		color_str = "donatello.jpg"
	elif color == "red":
		color_str = "raphael.jpg"
	else:
		color_str = "notapril.jpg"
	return render_template('single.html', color_string = color_str)
app.run(debug=True)