#17. 
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

# handle = open("test.txt", "w")
# handle.write('<hello')
# handle.close()

file = '''1)kazakstan
2)paris
3)uar
4)kyrgystan
5)san_francisco
6)germany
7)moscow
8)sweden'''

name = input('введите слово hello: ').lower().strip()

if name == 'hello':
    print('список городов:\n'+file)

    number = input('введите название или номер города: ').lower().strip()

    if number == '1' or number == 'kazakstan':
        handle = open("google_kazakstan.txt", "w")
        jaloba = input('введите вашу жалобу:')
        handle.write(jaloba)
        handle.close()

    elif number == '2' or number == 'paris':
        handle = open("google_paris.txt", "w")
        jaloba = input('введите вашу жалобу:')
        handle.write(jaloba)
        handle.close()

    elif number == '3' or number == 'uar':
        handle = open("google_uar.txt", "w")
        jaloba = input('введите вашу жалобу:')
        handle.write(jaloba)
        handle.close()

    elif number == '4' or number == 'kyrgystan':
        handle = open("google_kyrgystan.txt", "w")
        jaloba = input('введите вашу жалобу:')
        handle.write(jaloba)
        handle.close()

    elif number == '5' or number == 'san francisco':
        handle = open("google_san_francisco.txt", "w")
        jaloba = input('введите вашу жалобу:')
        handle.write(jaloba)
        handle.close()

    elif number == '6' or number == 'germany':
        handle = open("google_germany.txt", "w")
        jaloba = input('введите вашу жалобу:')
        handle.write(jaloba)
        handle.close()

    elif number == '7' or number == 'moscow':
        handle = open("google_moscow.txt", "w")
        jaloba = input('введите вашу жалобу:')
        handle.write(jaloba)
        handle.close()

    elif number == '8' or number == 'sweden':
        handle = open("google_sweden.txt", "w")
        jaloba = input('введите вашу жалобу:')
        handle.write(jaloba)
        handle.close()

    else:
        print('такого города под этим номером нет!!!')    
            
else:
    print('введите правильную команду!!!')




