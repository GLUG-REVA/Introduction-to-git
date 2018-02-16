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


def tri():
    rang = int(input("Enter the number of terms: "))
    ls = [0, 0, 1]
    i = 3
    while i < rang:
        d = ls[i - 1] + ls[i - 2] + ls[i - 3]
        ls.append(d)
        i += 1
    print(ls)

ls = ["1. Print Hello", "2. Fibonacci Series", "3. Prime Numbers", "4. Tribonacci Series"]
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
    tri()

else:
    print("Invalid option, noob")
