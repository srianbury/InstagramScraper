from flask import Flask, request, redirect, render_template
from os import urandom
from urllib2 import urlopen
import urllib
import re
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver

app = Flask(__name__)
app.config["SECRET_KEY"] = str(urandom(24));

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/greeting', methods = ["POST"])
def greeting():
	#POST_name = request.form["name"]
	url = request.form["name"]
	driver = webdriver.Firefox()
	driver.get(url)

	url_client = urlopen(url)
	page_html = url_client.read()

	soup = BeautifulSoup(driver.page_source, "html.parser")

	tags=soup.findAll('img')
	#print "\n".join(set(tag['src'] for tag in tags))
	link = tags[-1]['src'] 		

	#open link in new window
	#driver.get(link)
	
	return render_template("greeting.html", name = link)
	#return render_template("greeting.html", name = POST_name)

if __name__ == '__main__':
	app.run(debug = True)