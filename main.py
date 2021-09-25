from pprint import pprint

def get_cook_book(file_name):
    cook_book = {}
    with open(file_name) as file:
        for line in file:
            dish = line.strip()
            counter = int(file.readline())
            products = []

            for item in range(counter):
                ingredient, quantity, measure = file.readline().split(' | ')
                products.append(
                    {'ingredient_name': ingredient,
                     'quantity': int(quantity),
                     'measure': measure.strip()
                     }
                )

            cook_book[dish] = products
            file.readline()
    return cook_book

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    if isinstance(dishes, str):
        dishes = [dishes]
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name, measure, quantity = ingredient
            if name in shop_list.keys():
                shop_list[name]['quantity'] += quantity * person_count
            else:
                shop_list[name] = {'measure': measure,
                                   'quantity': quantity * person_count
                                   }
    return shop_list

cook_book = get_cook_book('cook_book.txt')

# pprint(cook_book)
pprint(get_shop_list_by_dishes(cook_book, 'Омлет', 2))
