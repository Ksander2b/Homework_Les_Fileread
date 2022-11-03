
with open('recipies.txt', 'rt') as file:
    cookbook = {}
    for line in file:
        dishes_name = line.strip()
        ingridients_count = int(file.readline())
        ingridients = []
        for _ in range(ingridients_count):
            ingridient = file.readline().strip().split(' | ')
            ingridient_name, quantity, measure = ingridient
            ingridients.append({'ingridient_name': ingridient_name, 'quantity': quantity,'measure': measure })
        file.readline()
        cookbook[dishes_name] = ingridients

# print(cookbook)

def get_shop_list_by_dishes(dishes_list, person_count):
    shoping_list = {}
    for keys, values in cookbook.items():
        if keys in dishes_list:
            for ing_dit in values:
                shoping_list[ing_dit.get('ingridient_name')] = {'measure': ing_dit.get('measure'), 
                'quantity': int(ing_dit.get('quantity')) * person_count}  

    return shoping_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
                


    



