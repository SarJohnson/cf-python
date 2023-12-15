import pickle

def display_recipe(recipe):
    print('recipe:', recipe['name'])
    print('cooking_time(min): ', recipe['cooking_time'])
    print('ingredients: ', recipe['ingredients'])
    print('diffuculy: ', recipe['difficulty'])

def search_ingredient(data): 
    all_ingredients = data['all_ingredients']
    all_ingredients_indexed = list(enumerate(all_ingredients, 1))

    for ingredient in all_ingredients_indexed:
        print('No.', ingredient[0], ' - ', ingredient[1])
        
    try:
        n = int(input("Select the corresponding number for the ingredient you would like: ")) 
        index = n - 1
        ingredient_search = all_ingredients[index]
        ingredient_search = ingredient_search.lower()
        
    except IndexError:
        print('The number you have chosen does not exist')
        
    except:
        print('Unexpected error occured')
        
    else:
        for recipe in data['recipes_list']:
                if ingredient_search in recipe['ingredients']:
                    print('\nThe following recipe includes the following ingredients')
                    display_recipe(recipe)

filename = input("please enter the filename with your recipes -") + ".bin"

try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)
    
except FileNotFoundError:
    print('this file does not exist in this directory')   
    data = { 'recipes_list':[], 'all_ingredients':[] } 

else:
    search_ingredient(data)
finally:
    recipes_file.close()