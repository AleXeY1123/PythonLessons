def func_str_byte(str_list):
    byte_list = []
    byte_num_list = []

    for i in str_list:
        byte_list.append(i.encode('utf-8'))

    for i in byte_list:
        byte_num_list.append(list(i))
    return byte_num_list

def func_byte_str(byte_list):
    str_list = []
    word_list_int = []

    for i in range(len(byte_list)):
        word_list = byte_list[i]
    
        for j in range(len(word_list)):
            try:
                word_list_int.append(int(word_list[j]))
            except ValueError:
                print(f'Значение "{word_list[j]}" не является числом, поэтому оно пропущено')

        word_list_bytes = bytes(word_list_int)
        word_list_int.clear()
        try:
            str_list.append(word_list_bytes.decode('utf-8'))
        except UnicodeDecodeError:
            print('Одно из значений введенного двухбайтного символа не является числом')

    return str_list
#--------------------------------------------------------------

str_or_byte = ''
while str_or_byte != '1' and str_or_byte != '2':
    str_or_byte = input('1 - из строки в байты, 2 - из байт в строку: ')

if str_or_byte == '1':
    in_list = input('Введите список строк через запятую: ')
    in_list = in_list.split(',')
    out_list = func_str_byte(in_list)

    print(out_list)

elif str_or_byte == '2':
    in_list = input('Введите список чисел через запятую, слова разделяются через точку с запятой: ')
    in_list = in_list.split(';')
    in_list_word = []
    for i in in_list:
        in_list_word.append(i.split(','))

    out_list = func_byte_str(in_list_word)

    print(out_list)

#-------------строки для проверки-----
#--1--
#12323,ghfggfgf,парара
#--2--
#49,50,51;103,102,103,102;208,191,208,176,208,191,208,176,209,128
#49,50,51;103,gfh,103,hgm;208,191,ggg,176,208,191,208,176,209,128