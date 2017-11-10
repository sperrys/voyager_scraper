import requests
import time

from contextlib import contextmanager
from flask import Flask
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

app = Flask(__name__)

@app.route('/')
def get_distance():

	URL = "https://voyager.jpl.nasa.gov/mission/status/"

	# Start the WebDriver and load the page
	wd = webdriver.Chrome()
	wd.get(URL)

	# Wait for the dynamically loaded elements to show up
	WebDriverWait(wd, 10).until(
    	EC.visibility_of_element_located((By.ID, "voy1_km")))

	# And grab the page HTML source
	html_page = wd.page_source
	wd.quit()

	# parse html to get distance
	soup = BeautifulSoup(html_page, "html.parser")
	distance = soup.find(id="voy1_km").get_text()
	
	sanitized = distance.split()[0]

	return sanitized
