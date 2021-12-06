def func_xor(in_text, key):
    out_str = ''
    for i in range(len(in_text)):
        j = 0
        if j == len(key):
            j = 0
        out_str += chr(ord(in_text[i]) ^ ord(key[j]))
        j += 1
    return out_str

try:
    command = int(input('1 - зашифровать, 2 - расшифровать: '))
except ValueError:
    print('Нужно ввести 1 или 2')
else:
    in_text = ''
    try:
        if command == 1:
            with open('Lesson6/task3_in-data-decrypted.txt','r') as f:
                in_text = f.read()
        elif command == 2:
            with open('Lesson6/task3_in-data-encrypted.txt','rb') as f:
                in_text = f.read()
                in_text = in_text.decode('utf-8')
    except FileNotFoundError:
        print('Нет файла с иходной строкой')
    else:
        key = input('Введите ключ: ')
        out_str = func_xor(in_text, key)
        print(out_str)

        if command == 1:
            with open('Lesson6/task3_in-data-encrypted.txt','wb') as f:
                f.write(out_str.encode('utf-8'))
        elif command == 2:
            with open('Lesson6/task3_in-data-decrypted.txt','w') as f:
                f.write(out_str)

# Australia has about forty kinds of bats.