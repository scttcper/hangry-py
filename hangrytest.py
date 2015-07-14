from __future__ import print_function
from hangrypy import hangry


def test_blueberry_muffins():
    h = hangry('http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html')
    assert h.recipe['canonical_url'] == 'http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html'
    assert h.recipe['name'] == 'Spinach and Mushroom Stuffed Chicken Breasts'
    assert h.recipe['description'] == 'Get this all-star, easy-to-follow Spinach and Mushroom Stuffed Chicken Breasts recipe from Rachael Ray'
    assert h.recipe['image_url'] == None
    assert h.recipe['ingredients'] == ['4 boneless, skinless chicken breasts, 6 ounces', 'Large plastic food storage bags or waxed paper', '1 package, 10 ounces, frozen chopped spinach', '2 tablespoons butter', '12 small mushroom caps, crimini or button', '2 cloves garlic, cracked', '1 small shallot, quartered', 'Salt and freshly ground black pepper', '1 cup part skim ricotta cheese', '1/2 cup grated Parmigiano or Romano, a couple of handfuls', '1/2 teaspoon fresh grated or ground nutmeg', 'Toothpicks', '2 tablespoons extra-virgin olive oil', '2 tablespoons butter', '2 tablespoons flour', '1/2 cup white wine', '1 cup chicken broth']
    assert h.recipe['instructions'] == ['Chicken', 'Dinner', 'Winter']
    assert h.recipe['prep_time'] == 900
    assert h.recipe['cook_time'] == 1200
    assert h.recipe['total_time'] == 2100
    assert h.recipe['published_date'] == None
    assert h.recipe['yield'] == 4




h = hangry('http://allrecipes.com/Recipe/Blueberry-Streusel-Muffins/Detail.aspx?evt19=1&referringHubId=2003')

print('canonical_url: ', h.recipe['canonical_url'])
print('name: ', h.recipe['name'])
print('description: ', h.recipe['description'])
print('image_url: ', h.recipe['image_url'])
print('ingredients: ', h.recipe['ingredients'])
print('instructions: ', h.recipe['instructions'])
print('prep_time: ', h.recipe['prep_time'])
print('cook_time: ', h.recipe['cook_time'])
print('total_time: ', h.recipe['total_time'])
print('published_date: ', h.recipe['published_date'])
print('yields: ', h.recipe['yield'])
print()