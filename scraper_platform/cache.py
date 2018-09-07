import time
from datetime import timedelta
import requests
import requests_cache
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class HTMLCache(object):
    '''Object that creates an HTMLCache that we can pass to Rules objects to use.'''
    def __init__(self, expiry: timedelta, cache: bool):
        self.expiry = expiry
        self.cache = cache
        requests_cache.install_cache(expire_after=self.expiry)

    def __repr__(self):
        return f'<HTMLCache object: expiry: {self.expiry}, {"cached" if self.cache else "uncached"}>'

    def create_browser(self):
        '''Creates a Chromium instance with some basic settings to load data into.'''
        # Set capabilities
        capabilities = DesiredCapabilities().CHROME
        capabilities["pageLoadStrategy"] = "normal"

        # Set options
        options = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images': 2, 'user-data-dir': 'C/'}
        options.add_experimental_option("prefs", prefs)

        return webdriver.Chrome(chrome_options=options, desired_capabilities=capabilities)

    def get_dynamic_html(self, url: str, delay=0):
        '''Gets the dynamic HTML of the page using a Chromium instance. Delay is how long we wait in seconds after page load to capture data.'''
        # Get the cache working here using selenium
        driver = self.create_browser()
        driver.get(url)

        # "Hack" to make the page fully load
        time.sleep(delay)
        return driver.page_source

    def get_html(self, url: str):
        """Gets the HTML of a webpage using requests, decode as UTF-8 and handle any HTTP errors"""
        if self.cache:
            try:
                # GET the webpage
                request = requests.get(url)
                html = request.content.decode('utf-8')

            # Handle any other errors
            except:
                print(f"URL error for {url}")
                return None
            return html
        else:
            with requests_cache.disabled():
                try:
                    # GET the webpage
                    request = requests.get(url)
                    html = request.content.decode('utf-8')

                # Handle any other errors
                except:
                    print(f"URL error for {url}")
                    return None
            return html
