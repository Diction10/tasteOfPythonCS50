#define main function
def main():
    x = int(input('x: '))
    y = int(input('y:'))
    z = maximum(x, y)
    print('Maximum is ', z)

#define maximum function
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
    
#call main function
main()