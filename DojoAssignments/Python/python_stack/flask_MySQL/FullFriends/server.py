from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():
	query = "SELECT first_name,id FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', friends=friends)

@app.route('/add', methods=['POST'])
def add():
	query = 'INSERT INTO friends (first_name,created_at,updated_at) VALUES(:first_name,NOW(),NOW())'
	data = {
		'first_name':request.form['name']
	}
	mysql.query_db(query,data)
	return redirect('/')
app.run(debug=True)