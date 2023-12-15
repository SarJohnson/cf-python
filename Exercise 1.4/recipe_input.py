import pickle

def take_recipe():
    name = str(input("Enter name of recipe: "))
    cooking_time = int(input("Enter cooking time in minutes: "))
    ingredients = input("Enter ingredients separated by commas: ").split(", ")
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients
    }
    recipe['difficulty'] = calc_difficulty(recipe)
    return recipe

def calc_difficulty(recipe):
    if recipe['cooking_time'] <= 90 and len(recipe['ingredients']) <= 5 : 
        difficulty = 'Easy'
    elif recipe['cooking_time'] <= 90 and len(recipe['ingredients']) > 5 : 
        difficulty = 'Intermediate'
    elif recipe['cooking_time'] > 90 and len(recipe['ingredients']) < 10 : 
        difficulty = 'Hard'
    elif recipe['cooking_time'] > 90 and len(recipe['ingredients']) >= 10 : 
        difficulty = 'Expert'
    return difficulty

recipes_list = []
all_ingredients = []

filename = input("Enter the filename you would like for your recipes: ") + ".bin"
data = { 'recipes_list':[], 'all_ingredients':[] }

try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)

except FileNotFoundError:
    print("file not found")

except:
    print("unexpected error")
    
else:
    recipes_file.close()
    
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

    n = int(input("How many recipes would you like to enter? "))

    for i in range(n):
        recipe = take_recipe()
        recipes_list.append(recipe)
        for ingredient in recipe['ingredients']:
            if not ingredient in all_ingredients:
                all_ingredients.append(ingredient)

data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}

recipes_file = open(filename, 'wb')
pickle.dump(data, recipes_file)
print('your file has been updated.')