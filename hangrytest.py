from __future__ import print_function
from hangrypy import Hangry


def test_spinach_mushroom_stuff_chicken():
    h = Hangry(url='http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html')
    assert h.recipe['canonical_url'] == 'http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html'
    assert h.recipe['name'] == 'Spinach and Mushroom Stuffed Chicken Breasts'
    assert h.recipe['description'] == 'Get this all-star, easy-to-follow Spinach and Mushroom Stuffed Chicken Breasts recipe from Rachael Ray'
    assert h.recipe['image_url'] == 'http://foodnetwork.sndimg.com/content/dam/images/food/fullset/2011/4/19/1/FN_chicken-breasts-006_s4x3.jpg.rend.sni12col.landscape.jpeg'
    assert h.recipe['ingredients'] == ['4 boneless, skinless chicken breasts, 6 ounces', 'Large plastic food storage bags or waxed paper', '1 package, 10 ounces, frozen chopped spinach', '2 tablespoons butter', '12 small mushroom caps, crimini or button', '2 cloves garlic, cracked', '1 small shallot, quartered', 'Salt and freshly ground black pepper', '1 cup part skim ricotta cheese', '1/2 cup grated Parmigiano or Romano, a couple of handfuls', '1/2 teaspoon fresh grated or ground nutmeg', 'Toothpicks', '2 tablespoons extra-virgin olive oil', '2 tablespoons butter', '2 tablespoons flour', '1/2 cup white wine', '1 cup chicken broth']
    assert h.recipe['instructions'] == ["Place breasts in the center of a plastic food storage bag or 2 large sheets of waxed paper. Pound out the chicken from the center of the bag outward using a heavy-bottomed skillet or mallet. Be firm but controlled with your strokes.","Defrost spinach in the microwave. Transfer spinach to a kitchen towel. Twist towel around spinach and wring it out until very dry. Transfer to a medium-mixing bowl.","Place a nonstick skillet over moderate heat. When skillet is hot, add butter, mushrooms, garlic and shallot. Season with salt and pepper and saute 5 minutes. Transfer mushrooms, garlic and shallot to the food processor. Pulse to grind the mushrooms and transfer to the mixing bowl, adding the processed mushrooms to the spinach. Add ricotta and grated cheese to the bowl and the nutmeg. Stir to combine the stuffing. Return your skillet to the stove over medium high heat.","Place a mound of stuffing on each breast and wrap and roll breast over the stuffing. Secure breasts with toothpicks. Add 3 tablespoons oil to the pan, 3 turns of the pan. Add breasts to the pan and brown on all sides, cooking chicken 10 to 12 minutes. The meat will cook quickly because it is thin. Remove breasts; add butter to the pan and flour. Cook butter and flour for a minute, whisk in wine and reduce another minute. Whisk in broth and return breasts to the pan. Reduce heat and simmer until ready to serve. Remove toothpicks. Serve breasts whole or, remove from pan, slice on an angle and fan out on dinner plates. Top stuffed chicken breasts or sliced stuffed breasts with generous spoonfuls of the sauce."]
    assert h.recipe['prep_time'] == 900
    assert h.recipe['cook_time'] == 1200
    assert h.recipe['total_time'] == 2100
    assert h.recipe['published_date'] == None
    assert h.recipe['yields'] == 4
    assert h.recipe.author == 'Rachael Ray'
    assert type(h.recipe.to_json()) == dict

def test_blueberry_muffins():
    h = Hangry('http://allrecipes.com/Recipe/Blueberry-Streusel-Muffins/Detail.aspx?evt19=1&referringHubId=2003')
    assert h.recipe['canonical_url'] == 'http://allrecipes.com/recipe/blueberry-streusel-muffins/'
    assert h.recipe['name'] == 'Blueberry Streusel Muffins'
    assert h.recipe['description'] == '"This recipe can be made with streusel or plain sugar topping. These muffins don\'t last long in our house. They are a favorite among my family and friends."'
    assert h.recipe['image_url'] == 'http://images.media-allrecipes.com/userphotos/250x250/00/17/70/177004.jpg'
    assert h.recipe['ingredients'] == ['1/2 cup butter, softened', '3/4 cup white sugar', '2 eggs', '1 teaspoon vanilla extract', '2 cups all-purpose flour', '2 teaspoons baking powder', '1/2 teaspoon salt', '1/2 cup milk', '1 1/2 cups blueberries', '2 tablespoons all-purpose flour', '2 tablespoons brown sugar', '1/4 teaspoon ground cinnamon', '2 tablespoons butter, chilled']
    assert h.recipe['instructions'] == ['Preheat oven to 375 degrees F (190 degrees C). Grease muffin cups or line with paper muffin liners.', 'In a large bowl, cream together the butter and sugar until light and fluffy. Stir in the eggs one at a time, beating well with each addition, then stir in the vanilla. In a separate bowl, stir together 2 cups flour, baking powder, and salt.', 'Stir the flour mixture into egg mixture alternately with milk. Fold in blueberries. Spoon batter into prepared muffin cups. In a small bowl, mix together 2 tablespoons flour, brown sugar and cinnamon. Cut in butter until mixture resembles coarse crumbs. Sprinkle topping over unbaked muffins.', 'Bake in preheated oven for 25 to 30 minutes, until a toothpick inserted into the center of a muffin comes out clean.']
    assert h.recipe['prep_time'] == 1200
    assert h.recipe['cook_time'] == 1800
    assert h.recipe['total_time'] == 3000
    assert h.recipe['published_date'] == None
    assert h.recipe['yields'] == 1
    assert h.recipe['yield_modifier'] == 'dozen'
    assert h.recipe.author == 'Carol Semenuk'
    assert type(h.recipe.to_json()) == dict


def test_apple_crisp():
    h = Hangry('http://allrecipes.com/Recipe/Apple-Crisp-II/Detail.aspx?evt19=1&referringHubId=1')
    assert h.recipe['canonical_url'] == 'http://allrecipes.com/recipe/apple-crisp-ii/'
    assert h.recipe['name'] == 'Apple Crisp II'
    assert h.recipe['description'] == 'This satisfying warm dessert goes perfectly with vanilla ice cream.'
    assert h.recipe['image_url'] == 'http://images.media-allrecipes.com/userphotos/250x250/00/27/70/277070.jpg'
    assert h.recipe['ingredients'] == ['10 cups all-purpose apples, peeled, cored and sliced', '1 cup white sugar', '1 tablespoon all-purpose flour', '1 teaspoon ground cinnamon', '1/2 cup water', '1 cup quick-cooking oats', '1 cup all-purpose flour', '1 cup packed brown sugar', '1/4 teaspoon baking powder', '1/4 teaspoon baking soda', '1/2 cup butter, melted']
    assert h.recipe['instructions'] == ['Preheat oven to 350 degrees F (175 degree C).', 'Place the sliced apples in a 9x13 inch pan. Mix the white sugar, 1 tablespoon flour and ground cinnamon together, and sprinkle over apples. Pour water evenly over all.', 'Combine the oats, 1 cup flour, brown sugar, baking powder, baking soda and melted butter together. Crumble evenly over the apple mixture.', 'Bake at 350 degrees F (175 degrees C) for about 45 minutes.']
    assert h.recipe['prep_time'] == 1800
    assert h.recipe['cook_time'] == 2700
    assert h.recipe['total_time'] == 4800
    assert h.recipe['published_date'] == None
    assert h.recipe['yields'] == 1
    assert h.recipe['yield_modifier'] == '9x13-inch pan'
    assert h.recipe.author == 'Diane Kester'
    assert type(h.recipe.to_json()) == dict
    