# -*- coding: utf-8 -*-
"""
    hangrypy
    ~~~~~~~~~~
    Description
"""
from json import dumps
from urllib2 import quote, urlopen, urlparse

from .default_recipe_parser import recipe_parser
from .non_standard.allrecipes import allrecipes
from .schema_org_recipe_parser import schema_org_recipe_parser, use_schema_org

parsers = {
    'schema_org_recipe_parser': schema_org_recipe_parser
}

non_standard = {
    'allrecipes.com': allrecipes
}

recipe = [
    'cook_time',
    'prep_time',
    'total_time',

    'canonical_url',
    'description',
    'image_url',
    'ingredients',
    'instructions',
    'name',
    'published_date',
    'yield',
]


class hangry(object):

    def __init__(self, url, parser=None):
        self.url_setup(url)
        # recipe dictionarie
        self.recipe = {x: None for x in recipe}

        # open url
        self.html = urlopen(url).read()
        self.parser = self.select_parser(parser)(self.html, self.recipe, self)
        self.parse()

    def select_parser(self, parser):
        if parser:
            return parsers[parser]
        if self.domain in non_standard:
            return non_standard[self.domain]
        if use_schema_org(self.html):
            return schema_org_recipe_parser
        return recipe_parser

    def url_setup(self, url):
        # mostly copied from
        # https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/urls.py
        self.full_url = url
        if isinstance(url, unicode):
            url = url.encode('utf-8', 'ignore')
        scheme, netloc, path, qs, anchor = urlparse.urlsplit(url)
        self.domain = netloc
        path = quote(path, '/%')
        # remove everything after path
        self.trimmed_url = urlparse.urlunsplit((scheme, netloc, path, '', ''))

    def parse(self):
        self.parser.parse_cook_time()
        self.parser.parse_prep_time()
        self.parser.parse_total_time()
        self.parser.parse_canonical_url()
        self.parser.parse_image_url()
        self.parser.parse_description()
        self.parser.parse_published_date()
        self.parser.parse_yields()
        self.parser.parse_name()
        self.parser.parse_instructions()
        self.parser.parse_ingredients()

    def to_json(self):
        return dumps(self.recipe)