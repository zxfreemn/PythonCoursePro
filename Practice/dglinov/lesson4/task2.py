'''
Составить программу, которая будет считывать введённое пятизначное число. После чего, каждую цифру этого числа необходимо вывести в новой строке:
Число: 10819
1 цифра равна 1
2 цифра равна 0
3 цифра равна 8
4 цифра равна 1
5 цифра равна 9
'''

if (x:=input("Введите 5ти значное число: ")).isdecimal() and len(x) == 5:
    for i in range(len(x)):                                                 #range() по умолчанию с 0
        print(f'{i+1} цифра равна {x[i]}')                                  #Условие задания:  Вывести строку в указанном формате "1 цифра равна 1"
else: 
    print("Нужно ввести 5ти значное число!")