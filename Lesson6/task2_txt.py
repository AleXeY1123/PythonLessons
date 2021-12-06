with open('Lesson6/task2_in-data.txt','r') as f:
    in_text = f.read()
in_text = in_text.replace(' ', '')
in_values = in_text.split(',')
_exit = False
for i in range(len(in_values)):
    try:
        in_values[i] = int(in_values[i])
    except ValueError:
        print('Введено некорректное значение')
        _exit = True

print(f'C: {in_values[0]}  H: {in_values[1]}  O: {in_values[2]}')
if not _exit:
    number_molecules = 0
    while in_values[0] >= 2 and in_values[1] >= 6 and in_values[2] >= 1:
        number_molecules += 1
        in_values[0] -= 2
        in_values[1] -= 6
        in_values[2] -= 1
    print(f'Количество молекул: {number_molecules}')
else:
    print('Программа завершена с ошибкой')