from scraper_platform import scraper, cache
from datetime import timedelta

s = scraper.Scraper(10, False)
print(s)

expiry = timedelta(days=2)
c = cache.HTMLCache(expiry, True)
print(c)
