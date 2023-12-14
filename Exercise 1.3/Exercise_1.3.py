recipes_list = []
ingredients_list = []

def take_recipe():
    name = str(input("Enter name of recipe: "))
    cooking_time = int(input("Enter cooking time in minutes: "))
    ingredients = input("Enter ingredients separated by commas: ").split(", ")
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    return recipe

n = int(input("How many recipes would you like to enter? "))

for i in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    for ingredient in recipe['ingredients']:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)

for recipe in recipes_list:
    if recipe['cooking_time'] <= 90 and len(recipe['ingredients']) <= 5 : 
        recipe['difficulty'] = 'Easy'
    elif recipe['cooking_time'] <= 90 and len(recipe['ingredients']) > 5 : 
        recipe['difficulty'] = 'Intermediate'
    elif recipe['cooking_time'] > 90 and len(recipe['ingredients']) < 10 : 
        recipe['difficulty'] = 'Hard'
    elif recipe['cooking_time'] > 90 and len(recipe['ingredients']) >= 10 : 
        recipe['difficulty'] = 'Expert'

    print('recipe:', recipe['name'])
    print('cooking_time(min): ', recipe['cooking_time'])
    print('ingredients: ', recipe['ingredients'])
    print('diffuculy: ', recipe['difficulty'])

ingredients_list.sort()
print('Ingredients available across all recipes:')
for ingredient in ingredients_list:
    print(ingredient)