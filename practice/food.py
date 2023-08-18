class Food:
    def __init__(self, name, protein, fat, carbs):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

    def calories(self):
        return (4 * int(self.carbs)) + \
            (4 * int(self.protein)) + \
            (9 * int(self.fat))

    def __str__(self):
        return self.name

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return str(self.name).capitalize()


# Recipes
print("Welcome to my Recipe Book")
print("Recipes".center(10))
print("-----------------")

redPasta = Recipe("red pasta", [Food("Noodles", 10, 10, 10), Food("Tomatoes", 4, 5, 13),
                                Food("Oil", 15, 1, 4)])
whitePasta = Recipe("white pasta", [Food("Noodles", 10, 10, 10), Food("Milk", 10, 10, 10),
                                    Food("Cheese", 3, 1, 20)])

recipes = redPasta, whitePasta
enumeratedRecipes = enumerate(recipes)

while True:
    for index, value in enumeratedRecipes:
        print(str(index) + ". ", value)

    response = input("Choose a recipe, Press q to quit: ")
    if response == 'q':
        break
    print()
    print()

    totalCalories = 0
    print(recipes[int(response)])
    print("-----")
    print("Ingredients: ")
    for ingredient in recipes[int(response)].ingredients:
        totalCalories += ingredient.calories()
        print(ingredient)

    print("Calories: " + str(totalCalories))
    print()

for recipe in recipes:
    totalCalories = 0
    print(recipe)
    for ingredient in recipe.ingredients:
        totalCalories += ingredient.calories()
    print("Calories: " + str(totalCalories))
    print()
