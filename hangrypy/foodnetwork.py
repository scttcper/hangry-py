from re import sub

from ..schema_org_recipe_parser import schema_org_recipe_parser


class foodnetwork(schema_org_recipe_parser):
    def parse_instructions(self):
        root = self.soup.find(attrs={'itemprop': 'recipeInstructions'})
        res = []
        for el in root.find_all('p', recursive=False):
            if el.has_attr('class') and el['class'][0] in ['copyright']:
                continue
            t = sub(r'[\t\r\n]', '', el.get_text())
            if len(t) > 2:
                res.append(t)
        return res or None

    def parse_image_url(self):
        el = self.soup.find(attrs={'itemprop': 'name'})
        name = el.get_text()
        el = self.soup.find(attrs={'alt': name})
        if el and el.has_attr('src'):
            return el['src']
