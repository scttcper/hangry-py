# hangry-py [![Coverage Status](https://coveralls.io/repos/scttcper/hangry-py/badge.svg?branch=master&service=github)](https://coveralls.io/github/scttcper/hangry-py?branch=master) [![Build Status](https://travis-ci.org/scttcper/hangry-py.svg?branch=master)](https://travis-ci.org/scttcper/hangry-py)
python port of https://github.com/iancanderson/hangry


To run tests ```coverage run --source=hangrypy setup.py test```

##Installation
```bash
pip install hangrypy
```

##example
```python
from hangrypy import Hangry
h = Hangry(url='http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html')

h.recipe.to_json() # returns dict of recipe

h.recipe.canonical_url # 'http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html'
h.recipe.name # 'Spinach and Mushroom Stuffed Chicken Breasts'
h.recipe.description # 'Get this all-star, easy-to-follow Spinach and Mushroom Stuffed Chicken Breasts recipe from Rachael Ray'
h.recipe['image_url'] # 'http://foodnetwork.sndimg.com/content/dam/images/food/unsized/Rachel_Ray.jpg.rend.sni2col.jpeg'
h.recipe.ingredients # ['4 boneless, skinless chicken breasts, 6 ounces', '...']
h.recipe.instructions # ["step 1", '...', 'step 3']
h.recipe['prep_time'] # 900
h.recipe.cook_time # 1200
h.recipe.total_time # 2100
h.recipe.published_date # None
h.recipe.yields # 4
h.recipe['yield_modifier'] # 'dozen'
```