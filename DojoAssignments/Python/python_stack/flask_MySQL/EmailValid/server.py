from flask import Flask, render_template, request, redirect, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, '')