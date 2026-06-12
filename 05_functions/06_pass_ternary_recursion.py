def fn1():
    pass


def fn2():
    pass


def fn3():
    pass


def is_even_number(number):
    # is_even = "Even" if number % 2 == 0 else "Odd"
    # return is_even
    return "Even" if number % 2 == 0 else "Odd"


print(is_even_number(11))


def gcd(a, b):
    # if b == 0:
    #     return a
    # else:
    #     return gcd(b, a % b)

    return a if b == 0 else gcd(b, a % b)


# def gcd(a, b): 
#     return "blaaaa"


print(gcd(100, 12))
