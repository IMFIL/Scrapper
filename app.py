from __future__ import print_function                 
from flask import Flask, render_template, request, url_for,Response,redirect
import urllib2
import json
import jinja2
from bs4 import BeautifulSoup
import math

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
	link = request.args.get('websiteLink')
	if link == None:
		return render_template('index.html')

	else:
		try:
			page = urllib2.urlopen(link).read()
		except ValueError:
			return "for now, you only get a string, but will make a error page :)"

		soup = BeautifulSoup(page,"html.parser")
		soup.prettify()
		print(soup)
		print(type(soup))
		return "done"

		# return a template that is exactly like index.html but has the results displayed in the search section


if __name__ =="__main__":
	app.run(debug=True)



















