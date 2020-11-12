# Tasks for beginners. Part II.
# Tasks Elementary for Python Course 
# (На английском языке что бы Вы научились понимать задачи) на английском языке)

# 1. 
# Write a program that greets the user by printing the word "Hello", a comma, the
# name of the user and an exclamation mark after it. See the examples below.
# Warning. Your program's output should strictly match the desired one,
# character by character. There shouldn't be any space between the name and
# the exclamation mark. You can use + operator to concatenate two strings.

# name = Shirin
# print('Hello, ', name, '!')


# 2. 
# N students take K apples and distribute them among each other evenly. The
# remaining (На английском языке что бы Вы научились понимать the undivisible) part remains in the basket. How many apples will
# each single student get? How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for
# the questions above. (На английском языке что бы Вы научились понимать Each N student will take K apples, and remains X)

# n = int(input('how many students?'))
# k = int(input('how many apples?'))
# print(k % n)


# 3. 
# Write a program that reads an integer number and prints its previous and
# next numbers. See the examples below for the exact format your answers
# should take. There shouldn't be a space before the period.
# Remember that you can convert the numbers to strings using the function str.
# (На английском языке что бы Вы научились понимать The next number for the number 179 is 180. The previous number for the
# number 179 is 178.)

# number = int(input('enter your number: '))
# print(number - 1)



# 4. 
# A timestamp is three numbers: a number of hours, minutes and seconds.
# Given two timestamps, calculate how many seconds is between them. The
# moment of the first timestamp occurred before the moment of the second
# timestamp. (На английском языке что бы Вы научились понимать 6, 1, 30, 6, 2, 10 result 40 sec.)

# hour1 = int(input('hour1 '))
# min1 = int(input('min1 '))
# sec1 = int(input('sec1 '))
# hour2 = int(input('hour2'))
# min2 = int(input('min2'))
# sec2 = int(input('sec2'))


# time1 = hour1*3600
# time2 = min1*60
# time3 = time1 + time2 + sec1

# time4 = hour2*3600
# time5 = min2*60
# time6 = time4 + time5 + sec2

# print(time6 - time3)



# 5. 
# A school decided to replace the desks in three classrooms. Each desk sits two
# students. Given the number of students in each class, print the smallest
# possible number of desks that can be purchased.
# - The program should read three integers: the number of students in each of
# the three classes, a, b and c respectively.
# - In the first test there are three groups. The first group has 20 students and
# thus needs 10 desks. The second group has 21 students, so they can get by
# with no fewer than 11 desks. 11 desks is also enough for the third group of
# 22 students. So we need 32 desks in total.

# class1 = int(input('введите число студентов:'))
# class2 = int(input('введите число студентов:'))
# class3 = int(input('введите число студентов:'))
# if class1 % 2 == 0:
#     print(class1 // 2)
# if class1 % 2 == 1:
#     print(class1 // 2 + 1)    
# if class2 % 2 == 0:
#     print(class2 // 2)
# if class2 % 2 == 1:
#     print(class2 // 2 + 1)  
# if class3 % 2 == 0:
#     print(class3 // 2)   
# if class3 % 2 == 1:
#     print(class3 // 2 + 1)       





# 6. 
# Given an integer. Print its tens digit.

# number = 3
# print(f'0,{number}')
 
 

# 7. 
# For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal
# to zero.
# Try to use the cascade if-elif-else for it.

# number = int(input('enter number: '))
# if number > 0:
#     print('1')
# elif number < 0:
#     print('-1')
# else:
#     print('0')


# 8. 
# Given two integers A and B (На английском языке что бы Вы научились понимать A ≤ B). Print all numbers from A to B inclusively.

# a = int(input('enter first number: '))
# b = int(input('enter second number: '))
# if a < b:
#     print(list(range(a,b+1)))


# 9. 
# In mathematics, the factorial of an integer n, denoted by n! is the following
# product:
# n!=1×2×...×n
# For the given integer n
# calculate the value n!. Don't use math module in this exercise

# n = int(input("Введите число"))
# factorial = 1
# for x in range(1, n + 1):
#     factorial *= x
#     print(factorial)


# 10. 
# You are given a string.
# In the first line, print the third character of this string.
# In the second line, print the second to last character of this string.
# In the third line, print the first five characters of this string.
# In the fourth line, print all but the last two characters of this string.
# In the fifth line, print all the characters of this string with even indices
# (На английском языке что бы Вы научились понимать remember indexing starts at 0, so the characters are displayed starting with
# the first).
# In the sixth line, print all the characters of this string with odd indices (На английском языке что бы Вы научились понимать i.e.
# starting with the second character in the string).
# In the seventh line, print all the characters of the string in reverse order.
# In the eighth line, print every second character of the string in reverse order,
# starting from the last one.
# In the ninth line, print the length of the given string.

# num = '0123456789'
# print(num[2])
# print(num[-2])
# print(num[0:4])
# print(num[:-2])
# print(num[::2])
# print(num[1::2])
# print(num[::-1])
# print(num[::-2])
# print(len(num))



# 11. 
# Given a string consisting of words separated by spaces. Determine how many
# words it has. To solve the problem, use the method count.

# text = 'my name is Shirin'
# b = text.split(' ')
# print(len(b))


# 12. 
# Given a string that may or may not contain a letter of interest. Print the index
# location of the first and last appearance of f. If the letter f occurs only once,
# then output its index. If the letter f does not occur, then do not print anything.
# Don't use loops in this task.

# text = 'my favourite tv show is GOT'
# if 'f' in text:
#     print(text.index('f'))
# else:
#     print("string 'f' not in text")    


# 13. 
# For a given integer N, print all the squares of integer numbers where the
# square is less than or equal to N, in ascending order.

# n = int(input('enter number:'))
# for i in range(1, n + 1):
#     print(i**2)


# 14. 
# Given a list of numbers, find and print all elements that are an even number. In
# this case use a for-loop that iterates over the list, and not over its indices! That
# is, don't use range(На английском языке что бы Вы научились понимать )

# number = [0,1,2,3,4,5,6,7,8,9]
# for i in number:
#     if i % 2 == 0:
#         print(i)


# 15. 
# Write the code, which will print numbers from 0 till your age. And if your age
# is odd, will be printed all odd numbers till your age, if even all even numbers.

# age = 20
# for i in range(1,age+1):
#     if i % 2 == 0:
#         print(i)
    


# 16. 
# If you were on the moon now, your weight will be 16,5% of your earth weight.
# To calculate it you have to multiple to 0,165. If next 15 years your weight will
# increase 1 kg each year. What will be your weight each year on the moon next
# 15 years?

# weight = 60
# inthemoon = 0.165
# through15year = weight * inthemoon
# print(through15year + 15)


# 17. 
# Write the code which will write excepted data to files below
# For example given offices of Google:
# 1) google_kazakstan.txt
# 2) google_paris.txt
# 3)google_uar.txt
# 4)google_kyrgystan.txt
# 5)google_san_francisco.txt
# 6)google_germany.txt
# 7)google_moscow.txt
# 8)google_sweden.txt
# When the user will say “Hello”
# Your code must communicate and give a choice from listed offices. After it
# has to receive a complain from user, and write it to file chosen by user.
# Hint: Use construction “with open”




# 18. 
# Hackerrank (На английском языке что бы Вы научились понимать https://www.hackerrank.com). Register and solve this problem
# right in it’s editor:
# Counting valleys: https://www.hackerrank.com/challenges/countingvalleys/problem

# 19. 
# Parsing (На английском языке что бы Вы научились понимать Has to be solved in two week(На английском языке что бы Вы научились понимать BootCamp week2 and week3))
# You have to Pars a site:
# https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/mobilnyetelefony
# As result you have to get
# . Name of product(На английском языке что бы Вы научились понимать title).
# . Price of product(На английском языке что бы Вы научились понимать KGS).
# . Link to photo.
# Write all info to csv file
# Extra: Your parser must do parsing each 60 minutes.

# HINT:
# 1)library beautiful soup
# 2)csv библиотека
# 3)library requests
# 4)datetime, time

# Usefull link to write this task:
# 1)https://www.youtube.com/watch?v=zlWiw99bBUk — это мощное видео про
# парсинг
# 2)https://www.crummy.com/software/BeautifulSoup/bs4/doc/ —документация
# beautiful soup
# 3)https://habr.com/ru/company/ods/blog/346632/ — практика парсинга
# (На английском языке что бы Вы научились понимать читать обязательно)
# 4)https://html5book.ru/osnovy-html/ — основы html для понимания
# 5)https://google.com
# 6)https://stackoverflow.com  ghbdtn

# Extra Bonus (На английском языке что бы Вы научились понимать Optional):
# 21. Напишите функцию которая будет суммировать введенные три случайные цифры.
# 22. Напишите функцию который будет конвертировать Фаренгейт в Цельсии и наоборот.
# 23. Напишите функцию котрый будет определять введенный год, высокосный или нет.
# 24. Напишите функцию которая будет определять полигдром ли введенная строка. Если да 2
# то печатать “True”, если нет “False”.
# 25. Напишите функцию которая находит самою длинную слово в строке.