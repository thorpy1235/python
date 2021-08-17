# -*- coding: utf-8 -*-

# prints first n triangular numbers
def triangle(n):
    num = 0
    for i in range(1, n + 1):
        num += i
        print(num)


user_num = int(input("Enter the number of triangular numbers to print: "))

print("The first {} triangular numbers are:".format(user_num))

triangle(user_num)