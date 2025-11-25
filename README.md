# Voyager 1 Web Scraper

This Flask webserver exposes a single route at '/' that scrapes the current distance (in miles) of the Voyager 1 probe from NASA's [Voyager Vital Signs](https://science.nasa.gov/mission/voyager/where-are-voyager-1-and-voyager-2-now/) page using Selenium, Beautiful Soup, and Chrome WebDriver.

## Setup

### Local Development (Mac)

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download ChromeDriver for Mac ARM64:
   - The app expects ChromeDriver in `chromedriver-mac-arm64/chromedriver`
   - Download from: https://googlechromelabs.github.io/chrome-for-testing/
   - Extract to the `chromedriver-mac-arm64/` directory
   - Note: This directory is gitignored and not deployed to Heroku

4. Run locally:
```bash
python voyager_scraper.py
```

### Heroku Deployment

The app uses platform detection:
- **Mac**: Uses local ChromeDriver from `chromedriver-mac-arm64/`
- **Heroku**: Uses Selenium Manager with the `heroku-buildpack-chrome-for-testing` buildpack

The buildpack automatically provides Chrome and ChromeDriver for the Linux environment.



