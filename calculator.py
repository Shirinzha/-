first = int(input('enter number: '))
operator = input('enter operator: ')
second = int(input('enter ur second number: '))
if operator == '*':
  result = first * second
  print(result)
elif operator == '/':
  print(first / second)
elif operator == '**':
  print(first ** second) 
elif operator == '//':
  print(first // second) 
elif operator == '+':
  print(first + second)   
elif operator == '-':
  print(first - second)   
elif operator == '%':
  print(first % second)
else:
  print('error')  










first = int(input('enter number: '))
operator = input('enter operator: ')
second = int(input('enter ur second number: '))
if operator == '*':
  result = first * second
  print(result)
elif operator == '/':
  if second == 0:
    print('na nol delit nelzya')
  elif second != 0:
    print(first / second)  
elif operator == '**':
  print(first ** second) 
elif operator == '//':
  print(first // second) 
elif operator == '+':
  print(first + second)   
elif operator == '-':
  print(first - second)   
elif operator == '%':
  print(first % second)
else:
  print('error')  
