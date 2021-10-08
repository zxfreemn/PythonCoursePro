"""
Составить программу, которая будет считывать введённое пятизначное число.
После чего, каждую цифру этого числа необходимо вывести в новой строке:
Число: 10819
1 цифра равна 1
2 цифра равна 0
3 цифра равна 8
4 цифра равна 1
5 цифра равна 9
"""

number = input("Enter the 5-digit number: ")
if len(number) == 5:
    for i, j in enumerate(number):
        print(f"{i+1} number is {j}")
else:
    print("Not 5-digit number.")