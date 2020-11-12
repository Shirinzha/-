"""
Задача №1
Напишите функцию is_even, которая принимает число 
и возвращает True, если оно четное, 
в противном случае - False. 

БОНУСНАЯ ЗАДАЧА: напишите решение функции 
в одной строке кода без использования операторов if.

"""
def is_even(number):
	#Напишите здесь свой код...
	

#Не удаляйте строки ниже, это сделано для проверки вашего кода.
def test_is_even():
	assert is_even(2) == True
	assert is_even(3) == False
	assert is_even(8) == True
	assert is_even(100) == True
	assert is_even(101) == False
	print("YOUR CODE IS CORRECT!")

#протестируйте свой код, не комментируя строки ниже
test_is_even()


"""
Задача №2
Напишите функцию square_number, 
которая берет число и возводит его в квадрат.
"""
def square_number(number):
	#Напишите здесь свой код...

#Не удаляйте строки ниже, это сделано для проверки вашего кода.
def test_square_number():
	assert square_number(2) == 4
	assert square_number(8) == 64
	assert square_number(10) == 100
	print("YOUR CODE IS CORRECT!")
test_square_number()


"""
Задача №3
Напишите функцию is_odd, которая принимает число 
и возвращает True, если оно нечетное, 
в противном случае - false. 

БОНУСНАЯ ЗАДАЧА: напишите решение функции в 
одной строке кода без использования операторов if.
"""
def is_odd(number):
	#Напишите здесь свой код...

#Не удаляйте строки ниже, это сделано для проверки вашего кода.
def test_is_odd():
	assert is_odd(2) == False
	assert is_odd(3) == True
	assert is_odd(8) == False
	assert is_odd(100) == False
	assert is_odd(101) == True
	print("YOUR CODE IS CORRECT!")

#протестируйте свой код, не комментируя строки ниже
test_is_odd()

"""
Задача №4
Напишите функцию last_letter, которая 
возвращает последнюю букву строки. 

Пример: last_letter ('hello!') # ->!

"""

def last_letter(word):
	#Напишите здесь свой код…

#Не удаляйте строки ниже, это сделано для проверки вашего кода.
def test_last_letter():
	assert last_letter('hello!') == '!'
	assert last_letter('banana') == 'a'
	assert last_letter('8') == '8'
	assert last_letter('funnyguys') == 's'
	assert last_letter('101') == '1'
	print("YOUR CODE IS CORRECT!")
#протестируйте свой код, не комментируя строки ниже
test_last_letter()


"""
Задача №5
Напишите функцию string_length, которая принимает строку 
и возвращает ее длину. 

ПОДСКАЗКА: Вопрос: Что вы имеете в виду под длиной? 
Ответ: количество символов в строке. 
Пример: string_length ('hello!') # -> 6 
Объяснение: вызов функции string_length () для строки 'hello!' должен вернуть мне 6.

"""
def string_length(word):
	#Напишите здесь свой код...

#Не удаляйте строки ниже, это сделано для проверки вашего кода.
def test_string_length():
	assert string_length('hello!') == 6
	assert string_length('banana') == 6
	assert string_length('8') == 1
	assert string_length('funnyguys') == 9
	assert string_length('101') == 3
	print("YOUR CODE IS CORRECT!")

#протестируйте свой код, не комментируя строки ниже
test_string_length()


