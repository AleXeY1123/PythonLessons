import re
def func(str_pass):
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