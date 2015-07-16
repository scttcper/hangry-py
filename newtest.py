import hangrypy
h = hangrypy.hangry('http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html')
print h.recipe['cook_time']