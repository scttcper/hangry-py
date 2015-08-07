from re import findall, sub

from .default_recipe_parser import recipe_parser


def use_schema_org(html):
    if 'http://schema.org/Recipe' in str(html):
        return True
    return False


class schema_org_recipe_parser(recipe_parser):
    def datetime_or_content(self, el):
        if el:
            if el.has_attr('datetime'):
                return self.parse_isoduration(el['datetime'])
            if el.has_attr('content'):
                return self.parse_isoduration(el['content'])
            return None
        else:
            return 0

    def parse_cook_time(self):
        el = self.soup.find(attrs={'itemprop': 'cookTime'})
        return self.datetime_or_content(el)

    def parse_prep_time(self):
        el = self.soup.find(attrs={'itemprop': 'prepTime'})
        return self.datetime_or_content(el)

    def parse_total_time(self):
        el = self.soup.find(attrs={'itemprop': 'totalTime'})
        return self.datetime_or_content(el)

    def parse_canonical_url(self):
        el = self.soup.find(attrs={'id': 'canonicalUrl'})
        if el and el.has_attr('href'):
            return el['href']

    def parse_image_url(self):
        el = self.soup.find(attrs={'itemtype': 'http://schema.org/Recipe'})
        if el:
            el = el.find(attrs={'itemprop': 'image'})
        if el and el.has_attr('src'):
            return el['src']

    def parse_description(self):
        el = self.soup.find(attrs={'itemprop': 'description'})
        if el:
            text = el.get_text() or el['content']
            return text.strip()

    def parse_published_date(self):
        el = self.soup.find(attrs={'itemprop': 'datePublished'})
        if el and el.has_attr('datetime'):
            return el.get_text()

    def parse_yields(self):
        el = self.soup.find(attrs={'itemprop': 'recipeYield'})
        if el:
            text = el.get_text() or el['content']
            y = findall(r'\d+', text.split(' ')[0])
            yields = int(y[0]) or 0
            yield_modifier = ' '.join(text.split(' ')[1:])
            return yield_modifier, yields

    def parse_instructions(self):
        root = self.soup.find(attrs={'itemprop': 'recipeInstructions'})

        res = []
        for el in root.find_all('li'):
            t = sub(r'[\t\r\n]', '', el.get_text())
            if len(t) > 2:
                res.append(t)
        return res or None

    def parse_ingredients(self):
        els = self.soup.find_all(attrs={'itemprop': 'ingredients'})
        res = []
        for el in els:
            t = el.get_text()
            t = sub('[\t\r\n]', '', t)
            t = sub("\s+", " ", t).strip()
            if len(t) > 2:
                res.append(t)
        return res or None

    def parse_name(self):
        el = self.soup.find(attrs={'itemprop': 'name'})
        if el:
            return el.get_text()

    def parse_author(self):
        el = self.soup.find(attrs={'itemprop': 'author'})
        if el:
            further = el.find(attrs={'itemprop': 'name'})
            if further:
                return further.get_text()
            else:
                return el.get_text()

