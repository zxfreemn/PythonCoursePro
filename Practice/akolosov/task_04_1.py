print('=' * 30 +'\n### The first way\n' + '=' * 30)

for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


print('\n' + '=' * 30 + '\n### The second way\n' + '=' * 30)

for i in ['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else
          'Buzz' if i % 5 == 0 else i for i in range(1, 101) ]:
    print(i)
