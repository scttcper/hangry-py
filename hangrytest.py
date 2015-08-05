from hangrypy import Hangry


def test_spinach_mushroom_stuff_chicken():
    recipe = Hangry(url='http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html')
    assert recipe['canonical_url'] == 'http://www.foodnetwork.com/recipes/rachael-ray/spinach-and-mushroom-stuffed-chicken-breasts-recipe.html'
    assert recipe['name'] == 'Spinach and Mushroom Stuffed Chicken Breasts'
    assert recipe['description'] == 'Get this all-star, easy-to-follow Spinach and Mushroom Stuffed Chicken Breasts recipe from Rachael Ray'
    assert recipe['image_url'] == 'http://foodnetwork.sndimg.com/content/dam/images/food/fullset/2011/4/19/1/FN_chicken-breasts-006_s4x3.jpg.rend.sni12col.landscape.jpeg'
    assert recipe['ingredients'] == ['4 boneless, skinless chicken breasts, 6 ounces', 'Large plastic food storage bags or waxed paper', '1 package, 10 ounces, frozen chopped spinach', '2 tablespoons butter', '12 small mushroom caps, crimini or button', '2 cloves garlic, cracked', '1 small shallot, quartered', 'Salt and freshly ground black pepper', '1 cup part skim ricotta cheese', '1/2 cup grated Parmigiano or Romano, a couple of handfuls', '1/2 teaspoon fresh grated or ground nutmeg', 'Toothpicks', '2 tablespoons extra-virgin olive oil', '2 tablespoons butter', '2 tablespoons flour', '1/2 cup white wine', '1 cup chicken broth']
    assert len(recipe['instructions']) == 4
    assert recipe['prep_time'] == 900
    assert recipe['cook_time'] == 1200
    assert recipe['total_time'] == 2100
    assert recipe['published_date'] == None
    assert recipe['yields'] == 4
    assert recipe.author == 'Rachael Ray'
    assert type(recipe.to_dict()) == dict
    assert type(recipe.to_json()) == str

def test_blueberry_muffins():
    recipe = Hangry('http://allrecipes.com/Recipe/Blueberry-Streusel-Muffins/Detail.aspx?evt19=1&referringHubId=2003')
    assert recipe['canonical_url'] == 'http://allrecipes.com/recipe/blueberry-streusel-muffins/'
    assert recipe['name'] == 'Blueberry Streusel Muffins'
    assert recipe['description'] == '"This recipe can be made with streusel or plain sugar topping. These muffins don\'t last long in our house. They are a favorite among my family and friends."'
    assert recipe['image_url'] == 'http://images.media-allrecipes.com/userphotos/250x250/00/17/70/177004.jpg'
    assert recipe['ingredients'] == ['1/2 cup butter, softened', '3/4 cup white sugar', '2 eggs', '1 teaspoon vanilla extract', '2 cups all-purpose flour', '2 teaspoons baking powder', '1/2 teaspoon salt', '1/2 cup milk', '1 1/2 cups blueberries', '2 tablespoons all-purpose flour', '2 tablespoons brown sugar', '1/4 teaspoon ground cinnamon', '2 tablespoons butter, chilled']
    assert recipe['instructions'] == ['Preheat oven to 375 degrees F (190 degrees C). Grease muffin cups or line with paper muffin liners.', 'In a large bowl, cream together the butter and sugar until light and fluffy. Stir in the eggs one at a time, beating well with each addition, then stir in the vanilla. In a separate bowl, stir together 2 cups flour, baking powder, and salt.', 'Stir the flour mixture into egg mixture alternately with milk. Fold in blueberries. Spoon batter into prepared muffin cups. In a small bowl, mix together 2 tablespoons flour, brown sugar and cinnamon. Cut in butter until mixture resembles coarse crumbs. Sprinkle topping over unbaked muffins.', 'Bake in preheated oven for 25 to 30 minutes, until a toothpick inserted into the center of a muffin comes out clean.']
    assert recipe['prep_time'] == 1200
    assert recipe['cook_time'] == 1800
    assert recipe['total_time'] == 3000
    assert recipe['published_date'] == None
    assert recipe['yields'] == 1
    assert recipe['yield_modifier'] == 'dozen'
    assert recipe.author == 'Carol Semenuk'
    assert type(recipe.to_dict()) == dict


def test_apple_crisp():
    recipe = Hangry('http://allrecipes.com/Recipe/Apple-Crisp-II/Detail.aspx?evt19=1&referringHubId=1')
    assert recipe['canonical_url'] == 'http://allrecipes.com/recipe/apple-crisp-ii/'
    assert recipe['name'] == 'Apple Crisp II'
    assert recipe['description'] == 'This satisfying warm dessert goes perfectly with vanilla ice cream.'
    assert recipe['image_url'] == 'http://images.media-allrecipes.com/userphotos/250x250/00/27/70/277070.jpg'
    assert recipe['ingredients'] == ['10 cups all-purpose apples, peeled, cored and sliced', '1 cup white sugar', '1 tablespoon all-purpose flour', '1 teaspoon ground cinnamon', '1/2 cup water', '1 cup quick-cooking oats', '1 cup all-purpose flour', '1 cup packed brown sugar', '1/4 teaspoon baking powder', '1/4 teaspoon baking soda', '1/2 cup butter, melted']
    assert recipe['instructions'] == ['Preheat oven to 350 degrees F (175 degree C).', 'Place the sliced apples in a 9x13 inch pan. Mix the white sugar, 1 tablespoon flour and ground cinnamon together, and sprinkle over apples. Pour water evenly over all.', 'Combine the oats, 1 cup flour, brown sugar, baking powder, baking soda and melted butter together. Crumble evenly over the apple mixture.', 'Bake at 350 degrees F (175 degrees C) for about 45 minutes.']
    assert recipe['prep_time'] == 1800
    assert recipe['cook_time'] == 2700
    assert recipe['total_time'] == 4800
    assert recipe['published_date'] == None
    assert recipe['yields'] == 1
    assert recipe['yield_modifier'] == '9x13-inch pan'
    assert recipe.author == 'Diane Kester'
    assert type(recipe.to_dict()) == dict
    