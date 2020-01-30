''''
Name: Brandon West
Student Number: 991179860
Program: Bachelors of Applied Information Security Systems
Class: Introduction to Crypto
Instructor: Joshua Schneider
Date: Monday 2-4 and Wednesday 4-6
'''

import math
def main():
    print("temp")
    breakCrypto()


def breakCrypto():
    print("crypto")
    p = 2625242353
    tripleTotient(p)


def tripleTotient(p):
    possibleArray = []
    print("Break it")
    sqrtP = int(math.sqrt(p))
    print(sqrtP)
    for i in range(0, sqrtP-1):
        prime = checkPrime(i)
        if prime:
            possibleArray.append(prime)
    print(possibleArray)


def checkPrime(number):
    # print("Prime")
    # Flag for is prime
    primeFlag = 0
    for i in range(2, number):
        if number % i == 0:
            primeFlag = 1
            break
        elif number % number == 0 and primeFlag != 1:
            return number


if __name__ == '__main__':
    main()
