from bs4 import BeautifulSoup

from .default_recipe_parser import recipe_parser
from .foodnetwork import foodnetwork
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

non_standard = {'foodnetwork.com': foodnetwork}


def url_setup(url):
        scheme, netloc, path, qs, anchor = urlsplit(url)
        domain = '.'.join(netloc.split('.')[-2:])
        path = quote(path, '/%')
        # remove everything after path
        url = urlunsplit((scheme, netloc, path, '', ''))
        return url, domain


def select_parser(html, parser, domain):
    if parser:
        return parsers[parser]
    if domain in non_standard:
        return non_standard[domain]
    if use_schema_org(html):
        return schema_org_recipe_parser
    return recipe_parser


def Hangry(url, html=None, parser=None):
    # open url or use passed
    if not html:
        html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html5lib')
    url, domain = url_setup(url)
    parser = select_parser(html, parser, domain)(soup)
    recipe = Recipe(parser, domain, url)
    return recipe
