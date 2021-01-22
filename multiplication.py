def main():
    for i in range (13):
        for j in range(13):
            multiply(i, j)

def multiply(x, y):
    product = x * y
    print(x, '*', y, '= ', product)

main()

