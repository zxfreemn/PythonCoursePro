import os
import time


def path_deleter(path_name):
    now = time.time()
    file_lifetime = 1
    dir_lifetime = 2
    for obj in os.listdir(path_name):
        abs_obj = os.path.join(path_name, obj)
        if os.path.isfile(abs_obj):
            if now - os.path.getctime(abs_obj) > file_lifetime:
                print(f'del file {abs_obj} lifetime {now - os.path.getctime(abs_obj)}')
                os.remove(abs_obj)
        elif os.path.isdir(abs_obj) and len(os.listdir(abs_obj)):
            path_deleter(abs_obj)
        elif os.path.isdir(abs_obj) and not len(os.listdir(abs_obj)):
            if now - os.path.getctime(abs_obj) > dir_lifetime:
                print(f'del dir {abs_obj} lifetime {now - os.path.getctime(abs_obj)}')
                os.rmdir(abs_obj)


def time_path_deleter(path_name):
    while True:
        path_deleter(path_name)
        if not len(os.listdir(path_name)):
            break


path = 'test'
if not os.path.exists(path):
    os.mkdir(path)
os.mkdir(os.path.join(path, 'test1'))
os.mkdir(os.path.join(path, 'test2'))
with open(os.path.join(path, 'test1', 'text1.txt'), 'w') as f1:
    f1.write('text1')
with open(os.path.join(path, 'text1.txt'), 'w') as f1:
    f1.write('text1')

time_path_deleter(path)



