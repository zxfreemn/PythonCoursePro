'''
Реализовать цикл, формирующий число из вводимых пользователем символов,
пока не будет введено слово “stop” (или “Stop”, или “STOP”).
Если пользователь ввел не числовой символ, вывести предупреждение и запросить новый символ.
'''

buf = ''

while True:
    res = input(f"Введите число: ")

    if res.lower() == 'stop':
        print(f'Конец работы программы. {buf}' )
        break
    if res.isdigit():
        print(f'Вы ввели: {res}')
        buf += res
    else:
        print(f'Вы ввели {res}, а должны ввести число:')