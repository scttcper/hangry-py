from json import dumps

from bs4 import BeautifulSoup

from .default_recipe_parser import recipe_parser
from .non_standard.allrecipes import allrecipes
from .non_standard.foodnetwork import foodnetwork
from .recipe import Recipe
from .schema_org_recipe_parser import schema_org_recipe_parser, use_schema_org

# messy python 3 support
try:
    from urllib.request import urlopen, quote
    from urllib.parse import urlunsplit, urlsplit
except ImportError:
    from urllib2 import urlopen, quote
    from urlparse import urlsplit, urlunsplit

parsers = {'schema_org_recipe_parser': schema_org_recipe_parser}

non_standard = {'allrecipes.com': allrecipes, 'foodnetwork.com': foodnetwork}


class Hangry(object):
    def __init__(self, url, html=None, parser=None):
        self.url_setup(url)

        # open url or use passed
        if not html:
            html = urlopen(url).read()
        soup = BeautifulSoup(html, 'html5lib')
        self.parser = self.select_parser(html, parser)(soup)
        self.recipe = Recipe(self.parser, url)

    def select_parser(self, html, parser):
        if parser:
            return parsers[parser]
        if self.domain in non_standard:
            return non_standard[self.domain]
        if use_schema_org(html):
            return schema_org_recipe_parser
        return recipe_parser

    def url_setup(self, url):
        self.full_url = url
        scheme, netloc, path, qs, anchor = urlsplit(url)
        self.domain = '.'.join(netloc.split('.')[-2:])
        path = quote(path, '/%')
        # remove everything after path
        self.trimmed_url = urlunsplit((scheme, netloc, path, '', ''))

    def to_json(self):
        return dumps(self.recipe)
