'''
Функции на вход подаётся последовательность чисел source и множитель m. 
На выходе функции ожидается новая последовательность на основе source, 
где каждый член был умножен на m. Если source не был указан, 
то берётся последовательность [1,2,3]. 
Укажите ошибки, допущенные в данной функции, и предложите свою реализацию
'''

def multiplier(m = 1, source =(1, 2, 3)):     
    return [x * m for x in source]

print(multiplier(5))
print(multiplier(12, [1, 2]))

