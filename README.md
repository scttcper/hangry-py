# hangry-py [![Coverage Status](https://coveralls.io/repos/scttcper/hangry-py/badge.svg?branch=master&service=github)](https://coveralls.io/github/scttcper/hangry-py?branch=master) [![Build Status](https://travis-ci.org/scttcper/hangry-py.svg?branch=master)](https://travis-ci.org/scttcper/hangry-py)
python port of https://github.com/iancanderson/hangry

##Installation
```bash
pip install hangrypy
```

To run tests ```coverage run --source=hangrypy setup.py test```

##example
```python
from hangrypy import Hangry
# returns a recipe object
recipe = Hangry(url='http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html')

recipe.to_dict() # returns python dict of recipe
recipe.to_json() # returns json dump of recipe

recipe.canonical_url # 'http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html'
recipe.name # 'Spinach and Mushroom Stuffed Chicken Breasts'
recipe.description # 'Get this all-star, easy-to-follow Spinach and Mushroom Stuffed Chicken Breasts recipe from Rachael Ray'
recipe['image_url'] # 'http://foodnetwork.sndimg.com/content/dam/images/food/unsized/Rachel_Ray.jpg.rend.sni2col.jpeg'
recipe.ingredients # ['4 boneless, skinless chicken breasts, 6 ounces', '...']
recipe.instructions # ["step 1", '...', 'step 3']
recipe['prep_time'] # 900
recipe.cook_time # 1200
recipe.total_time # 2100
recipe.published_date # None
recipe.yields # 4
recipe['yield_modifier'] # 'dozen'
```