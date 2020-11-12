for x in range (1,101):
    if x % 3 == 0 and x % 5 == 0:
        print('fuzzbuzz')
    elif x % 3 == 0:
        print('fuzz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print(x)


        # 1 * 2 * 3 *4 * 5
n = int(input("Введите число"))
factorial = 1
for x in range(1, n + 1):
    factorial *= x
    print(factorial)


средняя длина слов в икс
x = 'i need more exercises by python'
a = x.split(' ')
factorial = 0
for i in a:
  factorial += len(i)
print(factorial // len(a))