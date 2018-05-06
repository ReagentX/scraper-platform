import re
from scraper_platform import cache


class Rules(object):
    def __init__(self, cache: cache.HTMLCache):
        self.cache = cache

    def __repr__(self):
        return f'<Rules class using {self.cache}>'

    def get_links(self, url: str):
        html = self.cache.get_html(url)
        data = re.findall('<a href=\"(?:http://|https://)(.*?)\"', html)
        return data
