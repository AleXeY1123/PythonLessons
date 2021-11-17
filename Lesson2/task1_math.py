var1 = ""
var2 = ""
while not var1.replace('.', '', 1).isdigit():
  var1 = input('Введите первое число: ')

while not var2.replace('.', '', 1).isdigit():
  var2 = input('Введите второе число: ')

if var1.find('.') != -1:
  var1 = float(var1)
else:
  var1 = int(var1)

if var2.find('.') != -1:
  var2 = float(var2)
else:
  var2 = int(var2)

print(f'Сумма: {var1 + var2}')
print(f'Разность: {var1 - var2}')

print(f'Умножение: {var1 * var2}')

if var2 != 0:
  print(f'Деление: {var1 / var2}')
else:
  print(f'Деление: На 0 делить нельзя')

print(f'Степень: {var1 ** var2}')

if var2 != 0:
  print(f'Деление по модулю: {var1 % var2}')
else:
  print('Деление по модулю: На 0 делить нельзя')

if var2 != 0:
  print(f'Целочисленное деление: {var1 // var2}')
else:
  print('Целочисленное деление: На 0 делить нельзя')
