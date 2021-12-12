import re
def func(str_pass):
    '''Проверка на корректность пароля
    Пароль должен быть не менее 6 символов,
    Пароль должен содержать хотя бы одну цифру,
    Пароль не должен состоять только из цифр,
    Пароль не должен содержать слово password в любом регистре.
    Функция принимает любую строку
    '''
    if len(str_pass) < 6:
        return False

    elif len(re.findall(r'\d+', str_pass)) == 0:
        return False

    elif len(re.findall(r'\D+', str_pass)) == 0:
        return False

    elif str_pass.lower() == 'password': 
        return False

    else:
        return True
        
rez = func(input('введите пароль: '))

if rez:
    print('пароль подходит')
else:
    print('пароль не подходит')