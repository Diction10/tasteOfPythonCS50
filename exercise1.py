#Sum: Write a prog that asks the user to type in ten integers as input and then prints their sum

i = 0
x = 0
while i < 10:
    n = int(input('Number:'))
    i += 1
    x += n 
   
print('The sum of the ten number is: ', x)