'''
Реализовать алгоритм сортировки выбором. Алгоритм состоит из следующих шагов:
- найти наименьший элемент в массиве
- поменять местами его и первый элемент в массиве
- найти следующий наименьший элемент в массиве
- и поменять местами его и второй элемент массива
продолжать это пока весь массив не будет отсортирован
arr = [0,3,24,2,3,7]
// здесь реализованный алгоритм
// на выходе должен получиться список, содержащий [0, 2, 3, 3, 7, 24]
'''

data = [5,0,12,4,10,122,1488]

"""
Хорошо, но не эффективно, т.к. сначала мы ищем минимальный элемент, 
а потом в той же строке ищем его индекс (чудес тут, увы, нет: метод index тоже должен обходить строку). 
Если же мы будем запоминать индекс в том же цикле, где ищем минимум, алгоритм будет работать быстрее.
"""
def find_min_idx(lst):
    min_idx=0
    for idx, num in enumerate(lst):
        num_min = lst[min_idx]
        if num <= num_min:
            min_idx = idx
    return min_idx
    
def grab_and_sort(lst):
    for i in range(len(lst)):
        x = i + find_min_idx(lst[i:])
        lst[i], lst[x] = lst[x], lst[i]
        
grab_and_sort(data)
print(data)