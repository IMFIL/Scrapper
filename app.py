from __future__ import print_function                 
from flask import Flask, render_template, request, url_for,Response,redirect
import urllib2
import sqlite3 as lite
import json
import jinja2
import math

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


if __name__ =="__main__":
	app.run(debug=True)



















