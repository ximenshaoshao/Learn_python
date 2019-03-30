###test break in loop
##break means ends of the whole loop
def main():
    sum = 0
    number = 0
    while number < 20:
        number += 1
        sum += number
        if sum > 100:
            break
    print("The number is", number)
    print("The sum is", sum)
main()



###test continue in loop
##continue means ends of the loop and start the next one
def main2():
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
        print("Found a number", num)
main2()

###test else in loop
def main3():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
main3()