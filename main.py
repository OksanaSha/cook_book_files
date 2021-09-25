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

pprint(get_cook_book('cook_book.txt'))