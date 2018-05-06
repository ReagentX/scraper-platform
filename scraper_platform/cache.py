import re
from datetime import timedelta
import requests
import requests_cache


class HTMLCache(object):
    def __init__(self, expiry: timedelta, cache: bool):
        self.expiry = expiry
        self.cache = cache
        requests_cache.install_cache(expire_after=self.expiry)

    def __repr__(self):
        return f'<HTMLCache object: expiry: {self.expiry}, {"cached" if self.cache else "uncached"}>'

    def get_html(self, url):
        """Gets the HTML of a webpage, decoded as UTF-8 and handles any HTTP errors"""
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

                    # HLTV has a custom error page for HTTP errors
                    if len(re.findall('error-desc', html)) > 0 or len(re.findall('error-500', html)) > 0:
                        return None

                # Handle any other errors
                except:
                    print(f"URL error for {url}")
                    return None
            return html
