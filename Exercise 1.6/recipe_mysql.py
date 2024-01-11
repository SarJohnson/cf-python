import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS tasks_database")

cursor.execute("USE tasks_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)''')

def main_menu(conn, cursor):
    choice = ''
    while choice != 'quit':
        print("Main Menu")
        print("What would you like to do? Pick a choice!")
        print("1. Create a recipe")
        print("2. Search recipes")
        print("3. Update a recipe")
        print("4. Delete a recipe")
        print("5. Show all recipes")
        print("Type 'quit' to exit the program.")
        choice = input("Your choice: ")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            view_all_recipes(conn, cursor)

def create_recipe(conn, cursor):
    recipe_ingredients = []
    name = str(input("Enter name of recipe: "))
    cooking_time = int(input("Enter cooking time in minutes: "))
    ingredients = input("Enter ingredients separated by commas: ")
    recipe_ingredients = ingredients.split(", ")
    difficulty = calc_difficulty(cooking_time, recipe_ingredients)
    recipe_ingredients_str = ", ".join(recipe_ingredients)
    val = (name, recipe_ingredients_str, cooking_time, difficulty)
    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, val)
    conn.commit()
    print("recipe creation successful")
    
def calc_difficulty(cooking_time, recipe_ingredients):
        if cooking_time <= 90 and len(recipe_ingredients) <= 5:
            difficulty = 'Easy'
        elif cooking_time <= 90 and len(recipe_ingredients) > 5:
            difficulty = 'Intermediate'
        elif cooking_time > 90 and len(recipe_ingredients) < 10:
            difficulty = 'Hard'
        elif cooking_time > 90 and len(recipe_ingredients) >= 10:
            difficulty = 'Expert'
        print("difficulty: ", difficulty)
        return difficulty

def search_recipe(conn, cursor):
    all_ingredients = []
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall();
    for recipe_ingredients_list in results:
        for recipe_ingredients in recipe_ingredients_list:
            recipe_ingredients_split = recipe_ingredients.split(", " or ',')
            all_ingredients.extend(recipe_ingredients_split)
    all_ingredients = list(dict.fromkeys(all_ingredients))
    all_ingredients_list = list(enumerate(all_ingredients))
    print("List of all ingredients: ")
    for index, tup in enumerate(all_ingredients_list):
        print(str(tup[0]+1) + ". " + tup[1])
    try:
        ingredient_searched_num = input("Enter the number corresponding to the ingredient you want to select from the above list - ")
        ingredient_searched_index = int(ingredient_searched_num) - 1
        ingredient_searched = all_ingredients_list[ingredient_searched_index][1]
        print("You selected the ingredient: ", ingredient_searched)
    except:
        print("Make sure to select a number from the list.")
    else:
        print("The recipe(s) below include(s) the selected ingredient: ")
        cursor.execute("SELECT * FROM Recipes WHERE ingredients LIKE %s", ('%' + ingredient_searched + '%', ))
        results = cursor.fetchall()
        for row in results:
            print("id: ", row[0])
            print("name: ", row[1])
            print("cooking_time: ", row[2])
            print("ingredients: ", row[3])
            print("difficulty: ", row[4])

def update_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    recipe_id_for_update = int(input("Enter the ID of the recipe you would like to update - "))
    column_for_update = str(input("which one of these would you like to update? 'name', 'cooking_time', or 'ingredients - "))
    updated_value = input("Enter the new value for the recipe -  ")
    print("choice - ", updated_value)
    if column_for_update == "name":
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", (updated_value, recipe_id_for_update))
        print(column_for_update,"has been updated")
    elif column_for_update == "cooking_time":
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", (updated_value,recipe_id_for_update))
        cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id_for_update, ))
        result_recipe_for_update = cursor.fetchall()
        recipe_ingredients = tuple(result_recipe_for_update[0][2].split(','))
        cooking_time = result_recipe_for_update[0][3]
        updated_difficulty = calc_difficulty(cooking_time, recipe_ingredients)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s ", (updated_difficulty, recipe_id_for_update))
        print(column_for_update, " has been updated")
    elif column_for_update == "ingredients":
        cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", (updated_value, recipe_id_for_update))
        cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id_for_update, ))
        result_recipe_for_update = cursor.fetchall()
        recipe_ingredients = tuple(result_recipe_for_update[0][2].split(','))
        cooking_time = result_recipe_for_update[0][3]
        updated_difficulty = calc_difficulty(cooking_time, recipe_ingredients)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", (updated_difficulty, recipe_id_for_update))
        print(column_for_update, " has been updated")
    conn.commit()

def delete_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    recipe_to_delete = int(input("which recipe would you like to delete? - "))
    cursor.execute("DELETE FROM Recipes where id = (%s)", (recipe_to_delete, ))
    conn.commit()
    print("recipe has been deleted")

def view_all_recipes(conn,cursor):
    print("here is a list of all the recipes ")
    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()
    for row in results:
        print("id: ", row[0])
        print("name: ", row[1])
        print("ingredients: ", row[2])
        print("cooking_time: ", row[3])
        print("difficulty: ", row[4])
            
main_menu(conn, cursor)
print('bye')