cookbook = {}
def read_file_into_cookbook(cookbook_file):
    with open(cookbook_file) as book:
        while True:
            recipe_name = book.readline()
            if recipe_name is None or recipe_name == '':
                break
            recipe_name = recipe_name.strip()
            ingredients_count = int(book.readline())
            ingredients = []
            ingredient = {}
            while ingredients_count > 0:
                name, quantity, measure = book.readline().strip().split(" | ")
                ingredient = {"ingredient_name": name, "quantity": int(quantity), "measure": measure}
                ingredients.append(ingredient)
                ingredients_count -= 1
            cookbook[recipe_name] = ingredients
            book.readline()
    print(cookbook)

def get_shop_list_by_dishes(dishes: list, person_count: int):
    shopping_list = {}
    for dish in dishes:
        ingredients = cookbook[dish]
        for ingredient in ingredients:
            if ingredient["ingredient_name"] in shopping_list:
                shopping_list[ingredient["ingredient_name"]]["quantity"] += ingredient["quantity"]*person_count
            else:
                shopping_list[ingredient["ingredient_name"]] = {'measure': ingredient["measure"], 'quantity': ingredient["quantity"]*person_count}
    print(shopping_list) 

read_file_into_cookbook("cookbook.txt")
print('\n\n')
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4)
