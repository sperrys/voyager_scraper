import os

from flask import Blueprint
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

api = Blueprint('api', __name__)


@api.route('/')
def get_distance():

	# Updated URL - now using the iframe that contains the distance data
	URL = "https://science.nasa.gov/specials/apps/voyager-vital-signs/table/"


	opts = ChromeOptions()

	opts.add_argument('headless')
	opts.add_argument('--disable-gpu')
	opts.add_argument('--no-sandbox')

	# Get the path to the local chromedriver
	base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	chromedriver_path = os.path.join(base_dir, 'chromedriver-mac-arm64', 'chromedriver')
	service = Service(executable_path=chromedriver_path)

	# Start the WebDriver and load the page
	wd = Chrome(service=service, options=opts)
	wd.get(URL)

	# Wait for the dynamically loaded elements to show up
	WebDriverWait(wd, 20).until(EC.visibility_of_element_located((By.ID, "voy1_km")))

	# And grab the page HTML source
	html_page = wd.page_source
	wd.quit()

	# parse html to get distance (now in miles)
	soup = BeautifulSoup(html_page, "html.parser")
	distance = soup.find(id="voy1_km").get_text()

	# Extract just the number, removing commas
	# Format is like "15,791,867,050 mi"
	sanitized = distance.split()[0]
	no_commas = sanitized.replace(",", "")

	return no_commas
