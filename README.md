# Voyager 1 Web Scraper

This Flask webserver exposes a single route at '/' that
that uses the [voyager jpl website](https://voyager.jpl.nasa.gov/mission/status/) to scrape the current distance (in miles) of the Voyager 1
probe using selenium, beautiful soup, and the chrome webdriver to do the scraping of the dynamic content.

A live instance, although a bit slow, can be found at [https://voyagerscraper.herokuapp.com/](https://voyagerscraper.herokuapp.com/)


