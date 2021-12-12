x = 0
y = 0
direction=''
step = ''
while ((direction != 'вверх') and 
        (direction != 'вниз') and 
        (direction != 'влево') and 
        (direction != 'вправо')):
    direction = input('Введите направление (вверх, вниз, влево, вправо): ')
    
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