max_weight = 30
items = {'палка': 10, 
        'лопата':15, 
        'ложка': 3, 
        'тарелка':5, 
        'книга': 4, 
        'карандаш':2, 
        'куртка': 10, 
        'штаны':8, 
        'ботинки':6}
items_list = list(items.keys())
inventory = ['палка', 'книга', 'ботинки']
inventory_weight = 20
while True:
    in_command_item = input('Введите команду и название предмета через пробел или выход: ').split(' ')
    if in_command_item[0] == 'выход':
        break
    elif in_command_item[0] != 'добавить' and in_command_item[0] != 'удалить':
        print('Ошибка: недопустимая команда')
        continue
    else:
        command = in_command_item[0]

    item = in_command_item[1]

    if item not in items_list:
        print('Ошибка: такого предмета не существует')
    else:
        if command == 'добавить':
            if max_weight >= inventory_weight + items.get(item):
                inventory_weight += items.get(item)
                inventory.append(item)
            else:
                print('Ошибка: в инвентаре нет места для добавления этого предмета')
        if command == 'удалить':
            if item in inventory:
                inventory_weight -= items.get(item)
                inventory.remove(item)
            else:
                print('Ошибка: в инвентаре нет такого предмета')
    print(f'Сейчас содержится в инвентаре: ')
    for i in inventory:
        print(f'{i} : {items.get(i)}')
    print(f'Текущий вес инвентаря: {inventory_weight} \n')