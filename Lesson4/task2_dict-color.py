color_dict = {'red':(255, 0, 0), 'green':(0, 255, 0), 'blue':(0, 0, 255), 'black':(0, 0, 0), 'yellow':(255, 255, 0), 'cyan':(0, 255, 255), 'white':(255, 255, 255)}

color_in = input('Введите название цвета: ')
color_out = color_dict.get(color_in)
if color_out == None:
    print('Такого цвета в словаре нет')
else:
    print(f'Цвет в rgb: {color_out}')