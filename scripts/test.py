from scraper_platform import scraper, cache
from datetime import timedelta
from scraper_rules import sample_rules


# Create a scraper object
s = scraper.Scraper(3)
print(s)

# Create a cache object
expiry = timedelta(days=2)
c = cache.HTMLCache(expiry, True)
print(c)

# URL to test
urls = ['https://chrissardegna.com']

# Create the rules object based on the above cache object
r = sample_rules.Rules(c)
print(r)

# Create the rules object for a specific site
data = s.scrape(urls, r.get_links)
print(data)
