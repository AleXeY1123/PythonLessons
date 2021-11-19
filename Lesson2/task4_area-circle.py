import math
R = ""
while not R.replace('.', '', 1).isdigit():
  R = input('Введите радиус круга: ')

if R.find('.') != -1:
  R = float(R)
else:
  R = int(R)

S = math.pi * R**2
print(f'Площадь круга = {S}')