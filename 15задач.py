# Задача 1
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].

# # Выведите все элементы, которые меньше 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i <=5:
#         print(i)



# Задача 2
# Даны списки:

# a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
# b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
# c = a.intersection(b)
# print(c)


# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.


# Задача 3
# Посчитайте, сколько раз символ встречается в строке.

# s = 'You have a good attitude, in this session'
# print(s.count('a'))

# Задача 4
# Поменяйте значения переменных местами.

# a = 'sting'
# b = 9
# a,b = b,a
# print(a,b)

# Задача 5
# Нужно проверить, все ли числа в последовательности уникальны.

# a = [9, 1, 10, 4, 0, 5, 7]
# for i in a:
#     for j in range(i):
#         if i == j:
#             print('same')
#             quit()
#     print('unique')


# Задача 6 как делатььььь
# # Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# if a == b:
#     print(a,b)

# Задача 7
# При заданном целом числе n посчитайте n + nn + nnn.
#  numbers = ('5')*6
# print(numbers)

# Задача8
# Найдите три ключа с самыми высокими значениями в словаре . ????????????????????
# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
# for value in my_dict.values():
#     if value < 600:
#         abc = del value
#         print(abc)
# Задача9
# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# 1 2 2 3 3 3
# выходные данные
# 3


# a ={1, 2, 2, 3, 3, 3}
# print(len(a))



# Задача10
# Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.

# Программа получает на вход список, затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop().

# Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. Также нельзя использовать дополнительный список.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке. В следующей строке вводится одно целое число.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# 7 6 5 4 3 2 1 2
# выходные данные
# 7 6 4 3 2 1 



# a = [7, 6, 5, 4, 3, 2, 1, 2]
# a.pop(2)
# a.pop(-1)
# print(a)




# Задача11
# Дан список. Не изменяя его и не используя дополнительные списки, определите, какое число в этом списке встречается чаще всего.

# Если таких чисел несколько, выведите любое из них.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# 1 2 3 2 3 3
# выходные данные
# 3






# a = [1, 2, 2, 2, 1, 3, 2, 0, 2, 1, 3, 2, 4, 0, 4]
# most = 0
# most1 = 0
# for item in a:
#     most3 = a.count(item)
#     if most3 > most1:
#         most1 = most3
#         most = item 
# print(most)       






# Задача12
# Дан список целых чисел. Требуется “сжать” его, переместив все ненулевые элементы в левую часть списка, не меняя их порядок, 
# а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя,
#  задачу нужно выполнить за один проход по списку. Распечатайте полученный список.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# 4 0 5 0 3 0 0 5
# выходные данные
# 4 5 3 5 0 0 0 0 



# a = [4, 0, 5, 0, 3, 0, 0, 5]
# empty = 0
# notempty = 0
# for item in a:
#     if item == 0:
#         empty = item
#     elif item != 0:
#         print() порпобуй цикл в цикле, присвой числа больше нуля и сложи с эмпти     
# Задача13
# Найдите количество положительных (>0) элементов в данном списке.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# 1 -2 3 -4 5
# выходные данные
# 3



a = [1, -2, 3, -4, 5]
for item in range(1,a):
    print(item)
    # if item in a <= 0:     
    #     print(item)




# Задача14
# Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная, 
# то длина первой части должна быть на один символ больше). Переставьте эти две части местами,
#  результат запишите в новую строку и выведите на экран.

# При решении этой задачи нельзя пользоваться инструкцией if.

# Входные данные
# Вводится строка.

# Выходные данные
# Выведите ответ на задачу.

# Примеры
# входные данные
# Hi
# выходные данные
# iH
# входные данные
# Hello
# выходные данные
# loHel


# a = 'hi'


# Задача15
# Замена элементов списка
# Дан список целых чисел. Заменить отрицательные на -1, положительные - на число 1, ноль оставить без изменений.

# listOrigin = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
# itemm = 0
# itemmm = 0
# for item in listOrigin:
#     if item < 0:
#         itemm = item = -1
#     elif item > 0:
       





# Найти значение списка, которое встречается чаще всего
# Дан список. Определить в нем наиболее встречаемое значение.

# Программа ниже ищет только одно значение. Если в списке два значения встречаются с одинаковой частотой, 
# то будет определено только одно из них.

# [1, 2, 2, 2, 1, 3, 2, 0, 2, 1, 3, 2, 4, 0, 4]