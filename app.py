from __future__ import print_function                 
from flask import Flask, render_template, request, url_for,Response,redirect
import urllib2
import json
import jinja2
from bs4 import BeautifulSoup
import requests as RQ

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
	return render_template('index.html')



@app.route('/search/<url>')
def search():
	link = url

	headers = {'user-agent': 'Mozilla/5.0'}
	result = RQ.get(link,headers=headers)
	soup = BeautifulSoup(result.content,"html.parser")
	soup.prettify()
	print(soup)
	print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")		
	return "done"


		# return a template that is exactly like index.html but has the results displayed in the search section


if __name__ =="__main__":
	app.run(debug=True)



















