# -*- coding: utf-8 -*-

# prints first n prime numbers
def prime(n):
    if n < 1:
        return
    num_primes = 0
    num = 2
    while num_primes < n:
        if all([num % i != 0 for i in range(2, num)]):
            print(num)
            num_primes += 1
        num += 1
        
user_num = int(input("Enter the number of prime numbers to print: "))

print("The first {} prime numbers are:".format(user_num))

prime(user_num)
