from isodate import parse_duration


class recipe_parser(object):

    def __init__(self, soup):
        self.soup = soup

    # TODO: create a default recipe parser

    def parse_prep(self):
        pass

    def parse_isoduration(self, datetime):
        try:
            return int(parse_duration(datetime).total_seconds())
        except:
            try:
                return int(datetime)
            except:
                return None
