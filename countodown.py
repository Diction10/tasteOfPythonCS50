import time
import random

#define main function
def main():
    number = random.randint(5, 15)
    countdown(number)
    print('Happy New Year')

#define function countdown
def countdown(n):
    for i in range(n):
        print(n-i)
        time.sleep(1)

#call main function
main()



# x = 11
# for i in range(10):
#     i += 1
#     x -= 1
#     print(x)
# print('Happy New Year')

# for i in range(10):
#     print(10-i)
# print('A ku Odun o')