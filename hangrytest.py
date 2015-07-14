from __future__ import print_function
from hangrypy import hangry

h = hangry('http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html')

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
print()
print()

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