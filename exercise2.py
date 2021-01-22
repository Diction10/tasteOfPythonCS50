# guessing game

# Write a prog that picks a pseudorandom number between 1 and 10, inclusive
# and gives the user up to 3 chances to guess that number, each time printing
# some messages informing the user wherher or not their guess was correct.

import random
#get computer number
comp_number = random.randint(1, 10)

i = 0

while i < 3:
    #get user's number
    user_number = int(input('Guess a Number: '))
    if user_number < comp_number:
        print('Your number is lesser')
    elif user_number > comp_number:
        print('Your number is greater')
    else:
        print('You guessed correctly. Congrats!')
        break

    i +=1

    