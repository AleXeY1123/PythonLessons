x = 0
y = 0

while True:
    direction=''
    step = ''
    while ((direction != 'вверх') and 
            (direction != 'вниз') and 
            (direction != 'влево') and 
            (direction != 'вправо') and 
            (direction != 'выход')):
        direction = input('Введите направление (вверх, вниз, влево, вправо) или выход: ')

    if direction == 'выход':
        break

    while not step.isdigit():
        step = input('Введите количество шагов: ')

    step = int(step)
    if direction == 'вверх':
        y += step
    elif direction == 'вниз':
        y -= step
    elif direction == 'вправо':
        x += step
    elif direction == 'влево':
        x -= step

    print(f'Текущая позиция (x,y): ({x},{y})')