from bs4 import BeautifulSoup
from isodate import parse_duration


class recipe_parser(object):

    def __init__(self, html, r, parent):
        self.soup = BeautifulSoup(html, 'html5lib')
        self.recipe = r
        self.parent = parent

    # TODO: create a default recipe parser

    def parse_prep(self):
        pass

    def parse_isoduration(self, datetime):
        try:
            return int(parse_duration(datetime).total_seconds())
        except:
            pass
        try:
            return int(datetime)
        except:
            pass
        return None
