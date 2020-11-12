# x = [13, 10, 59, 89, 75, 29, 18, 13, 53]
# for a in x:
#     if str(x)[-1] == 9:
#         print(x)




# x = ['admin' , 'nik' , 'stan' , 'cole']
# def users(x):
#     for user in x:
#         if user == 'admin':
#             user1 = user.title()
#             print(f'Добро пожаловать, {user1}')
        
#         else:
#             print(f'Добро пожаловать {user}')    
# users(x)




def find_end():
  for x in range(1, 101):    
    if str(x)[-1] == 1: 
      print('попытка')
    elif str(x)[-1] == 2 and str(x)[-1] == 3 and str(x)[-1]==4:
      print('попытки') 

    else:
      print('попыток')
find_end()


def word():
    for words in range(1, 101):
        print(words)
word(x)        