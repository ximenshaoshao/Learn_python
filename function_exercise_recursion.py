##阶乘
def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)

def main():
    n = eval(input("Please enter a number <n> to calculate n!: "))
    print(fact(n))

main()