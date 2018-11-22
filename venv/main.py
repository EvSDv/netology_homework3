def pars_file():
    cook_book = {}
    with open('cook_book.txt', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            amt_ingridients = int(f.readline())
            cook_book[dish_name] = list()
            while amt_ingridients > 0:
                ingridient_name, quantity, measure = f.readline().strip().split(sep='|')
                cook_book[dish_name].append({'ingridient_name' : ingridient_name.strip(), 'quantity' : int(quantity), 'measure' : measure.strip()})
                amt_ingridients-= 1
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    ingridients = {}
    for dish in dishes:
        for recipe in pars_file()[dish]:
            if recipe['ingridient_name'] not in ingridients:
                ingridients[recipe['ingridient_name']] = {'measure' : recipe['measure'], 'quantity' : recipe['quantity'] * person_count}
            else:
                ingridients[recipe['ingridient_name']] = {'measure' : recipe['measure'], 'quantity' : (recipe['quantity'] * person_count) + ingridients.pop(recipe['ingridient_name'])['quantity']}
    return ingridients

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))