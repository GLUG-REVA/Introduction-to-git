#!usr/bin/python3


def fib():
    rang = int(input("Enter the number of terms: "))
    print("0, 1, ", end="")
    a, b, i = 0, 1, 3
    while i <= rang:
        c = a + b
        print(c, end=", ")
        a = b
        b = c
        i += 1


def prime():
    chk = 0
    num = int(input("Enter the number to be checked: "))
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print(str(num) + " is not a Prime number.")
            chk = 1
            break
    if chk == 0:
        print(str(num) + " is a Prime number.")


def factorial():
    product = 1
    num = int(input("Enter the number to print factorial: "))
    for i in range(2, num + 1):
        product *= i
    print("Factorial: " + str(product))

ls = ["1. Print Hello", "2. Fibonacci Series", "3. Prime Numbers", "4. Factorial of a number"]
for i in ls:
    print(i)

option = input("Enter your option: ")

if option == '1':
    print("Hello")

elif option == '2':
    fib()

elif option == '3':
    prime()

elif option == '4':
    factorial()

else:
    print("Invalid option, noob")
