import random

while True:
    xnum = 0
    rstart = input('Range start: ')
    if not rstart.replace('-', '').replace('.', '').isdigit():
        print(f'Wrong value: {rstart}')
        continue
    rend = input('Range end: ')
    if not rend.replace('-', '').replace('.', '').isdigit():
        print(f'Wrong value: {rend}')
        continue
    if int(rstart) < int(rend):
        xnum = random.randint(int(rstart), int(rend))
        print(f'В заданном диапазоне от {rstart} до {rend} загадано число. Угадайте его.({xnum=})')
    else:
        print(f'Некорректный диапазон. {rend=} должен быть больше {rstart=}')
        break
while True:
    n = input('Введите число или "stop" для выхода: ')
    nx = 0
    if n.replace('-', '').replace('.', '').isdigit():
        nx = int(n)
        if int(rstart) > nx or nx > int(rend):
            print('Вне диапазона!')
        elif nx > xnum:
            print('Слишком большое число')
        elif nx < xnum:
            print('Слишком маленькое число')
        elif nx == xnum:
            print('Угадали !!!')
            break
    elif n.lower() == 'stop':
        print('Stopped')
        break
    else:
        print(f'Wrong value: {n}')
        n = ''



