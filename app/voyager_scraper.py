import os

from flask import Blueprint
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By

api = Blueprint('api', __name__)


@api.route('/')
def get_distance():

	URL = "https://science.nasa.gov/mission/voyager/where-are-they-now/"


	opts = ChromeOptions()

	opts.add_argument('headless')
	opts.add_argument('--disable-gpu')
	opts.add_argument('--no-sandbox')

	# Start the WebDriver and load the page
	wd = Chrome(executable_path="chromedriver", chrome_options=opts)
	wd.get(URL)

	# Wait for the dynamically loaded elements to show up
	WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.ID, "voy1_km")))

	# And grab the page HTML source
	html_page = wd.page_source
	wd.quit()

	# parse html to get distance
	soup = BeautifulSoup(html_page, "html.parser")
	distance = soup.find(id="voy1_km").get_text()
	
	sanitized = distance.split()[0]
	no_commas = sanitized.replace(",", "")

	return no_commas
