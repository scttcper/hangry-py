class Recipe(object):

    def __init__(self, parser, url):
        self.parser = parser
        self._cook_time = None
        self._prep_time = None
        self._total_time = None
        self._canonical_url = url
        self._description = None
        self._image_url = None
        self._ingredients = None
        self._instructions = None
        self._name = None
        self._published_date = None
        self._yields = None
        self._yield_modifier = None

    @property
    def cook_time(self):
        if not self._cook_time:
            self._cook_time = self.parser.parse_cook_time()
        return self._cook_time

    @property
    def prep_time(self):
        if not self._prep_time:
            self._prep_time = self.parser.parse_prep_time()
        return self._prep_time

    @property
    def total_time(self):
        if not self._total_time:
            self._total_time = self.parser.parse_total_time()
        return self._total_time

    @property
    def canonical_url(self):
        self._canonical_url = self.parser.parse_canonical_url() or self._canonical_url
        return self._canonical_url

    @property
    def description(self):
        if not self._description:
            self._description = self.parser.parse_description()
        return self._description

    @property
    def image_url(self):
        if not self._image_url:
            self._image_url = self.parser.parse_image_url()
        return self._image_url

    @property
    def ingredients(self):
        if not self._ingredients:
            self._ingredients = self.parser.parse_ingredients()
        return self._ingredients

    @property
    def instructions(self):
        if not self._instructions:
            self._instructions = self.parser.parse_instructions()
        return self._instructions

    @property
    def name(self):
        if not self._name:
            self._name = self.parser.parse_name()
        return self._name

    @property
    def published_date(self):
        if not self._published_date:
            self._date = self.parser.parse_published_date()
        return self._published_date

    @property
    def yields(self):
        if not self._yields:
            self._yield_set()
        return self._yields

    @property
    def yield_modifier(self):
        if not self._yield_modifier:
            self._yield_set()
        return self._yield_modifier

    def _yield_set(self):
        self._yield_modifier, self._yields = self.parser.parse_yields()

    def __getitem__(self, key):
        return getattr(self, key)