# scraper-platform

A simple multiprocessed Python scraper platform powered by RegEx and `requests`.

## Classes

### HTMLCache

This class contains the methods to construct a cache of HTML information for scraping.

This class is constructed with a `timedelta` for the expiration length of the cache database and a boolean for whether the cache will be used or bypassed.

### Scraper

This class contains the methods to apply a set of `Rules()` to a list of URLs in multiple threads.

This class is constructed with an integer that sets the maximum number of threads.

### Rules

This class contains the code to parse URLs. It is initialized with an `HTMLCache` object. Rules classes must be kept in the `scraper_rules` module.

This class is constructed with an HTMLCache which the rules will use to get the HTML of webpages.

The class methods are rules that are designed to take a single URL and apply some transformation to it, then return a list of data.

## Examples

To install the package, download/clone it, `cd` to the directory, and run `python setup.py develop`.

This allows for fast testing of RegEx rules across a set of URLs. To begin, we need to import a few things:

    from scraper_platform import scraper, cache
    from datetime import timedelta
    from scraper_rules import sample_rules

Here, we import the `scraper` and `cache` modules from the `scraper_platform` module as well as the `sample_rules` module from the `scraper_rules` module. We also import the `timedelta` datatype so we can construct an `HTMLCache` object.

Next, we need to create the objects we imported:

    s = scraper.Scraper(2)
    c = cache.HTMLCache(timedelta(days=2), True)

Here, we create a Scraper object that will use at maximum two threads and a Cache object where the HTML cached will have an expiration of 2 days from access. Changing the boolean argument to false will bypass the cache altogether.

If we print `s` and `c` we should get:

    <Scraper object: max 2 threads>
    <HTMLCache object: expiry: 2 days, 0:00:00, cached>

Next, we can create our sample rules class and define a list of URLs to analyze. For this example I use Google's store page and some regex to capture all of the http/https links:

    r = sample_rules.Rules(c)
    urls = [
    'https://store.google.com/category/phones',
    'https://store.google.com/category/home_entertainment',
    'https://store.google.com/category/laptops_tablets',
    'https://store.google.com/category/virtual_reality'
    ]

To get the data, we then run the scraper by passing the list of URLs and the function we want to apply to them:

    data = s.scrape(urls, r.get_links)

This maps the URLs to the rule method `get_links` and returns a list of the data we asked for in a variable called `data`.