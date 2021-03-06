import sys
import os
import hashlib
import ast
import argparse
# Импорты модулей только для текущего проекта
#from time import *
from time import time

#Наименования классов в формате CamelCase
#class shuffler:
class Shuffler:
    def __init__(self):
        self.map = {}
#Определения методов внутри класса разделяются одной пустой строкой.

    def rename(self, dirname, output):
#          mp3s = []
# Выравнивание
        mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
#Чтобы проверка сработала убрать "."               
#                if file[-3:] == '.mp3':
                if file[-3:] == 'mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
#Имя метода класса изменилось            
            hashname = self.generate_name() + '.mp3'
            self.map[hashname] = mp3
#(function) rename: (src: StrOrBytesPath, dst: StrOrBytesPath, *, src_dir_fd: int | None = ..., dst_dir_fd: int | None = ...) -> Non
#            os.rename(path + '/' + mp3), path + '/' + hashname))          
            os.rename(path + '/' + mp3, path + '/' + hashname)
#Выравнивание + изменить Access Mode на запись r+
#        f = open(output, 'r')
        f = open(output, 'r+')
        f.write(str(self.map))
#Я бы еще закрыл файлик defer f.Close()
        f.close()
#Определения методов внутри класса разделяются одной пустой строкой.

# Название переменной не отражает суть
#    def restore(self, dirname, restore_path):
    def restore(self, dirname, filename):
#Выравнивание + ошибка в Access Mode r+ (read + write)
#          with open(filename, '+') as f:
        with open(filename, 'r+') as f:         
            self.map = ast.literal_eval(f.read())
#Выравнивание
#         mp3s = []
        mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
#Выравнивание + проверка на 3 символа с конца                
#               if file[-3:] == '.mp3':
                if file[-3:] == 'mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
#Лишняя скобочка            
#            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
             os.rename(path + '/' + hashname, path + '/' + self.map[hashname])
        os.remove(filename)
#Определения методов внутри класса разделяются одной пустой строкой.

#Название метода в формате some_function + выравнивание               
#     def generateName(self, seed=time()):
    def generate_name(self, seed=time()):
        return hashlib.md5(str(seed)).hexdigest()
#Отделяйте функции верхнего уровня и определения классов 
#двумя пустыми строками


#Для аргументов точно какой-то косяк
#По всей видимости для метода rename м.б. 2 варианта: default("restore.info") 
#и конкретный путь до файла ("-o path").
#Проверку в main() можно убрать добавив значение по умолчанию для аргумента
def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
#Название переменной в нижнем регистре
#    Shuffler = shuffler()
    shuffler = Shuffler()
    if args.subcommand == 'rename':
# Если output указан то "сбрасываем" в него
          if args.output:
                shuffler.rename(args.dirname, args.output)
          else:
                shuffler.rename(args.dirname, 'restore.info')
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()