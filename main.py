with open('recipies.txt', 'rt') as file:
    dishes = []
    for line in file:
        dishes_name = line.strip()
        ingridients_count = int(file.readline())
        ingridients = []
        for _ in range(ingridients_count):
            ingridient = file.readline().strip().split(' | ')
            ingridient_name, quantity, measure = ingridient
            ingridients.append({'ingridient_name': ingridient_name, 'quantity': quantity,'measure': measure })
        file.readline()
        cookbook = {dishes_name: ingridients }
        dishes.append(cookbook)

print(dishes)

