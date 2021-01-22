# Write a prog that asks the user to 
# type in a number and then prints an n x n grid of hash marks

n = int(input('Type a number: '))

for i in range(n):
    for j in range(n):
        print('#', end="") 
    print()
