import math


a = int(input("Введите первое натуральное число: "))
b = int(input("Введите второе натуральное число: "))


def NOD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print (("НОД:"), a)
    return a


t = NOD(a, b)



def NOK(a, b):
    a = a * b // t
    print(("НОД:"), a)


NOK(a, b)


number = int(input())
number2 = number
factors = []
d = 2


def Primenumberdecomposition(number, d):
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i

    if number != 1:
        factors.append(number)

    print('{} = {}'.format(number2, factors))


t = Primenumberdecomposition(number, d)