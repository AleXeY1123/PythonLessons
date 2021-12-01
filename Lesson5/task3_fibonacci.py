def fibonacci(quantity, current, xn1, xn2):
    x = xn1 + xn2
    xn1 = xn2
    current = current + 1
    if current == quantity-1:
        return
    print(x)
    fibonacci(quantity, current, xn1, x)

while True:
  try:
    quantity= int(input('Введите количество членов последовательности: '))
    break
  except ValueError:
      print('Нужно ввести целое число')

print('0')
print('1')
fibonacci(quantity, 0, 0, 1)