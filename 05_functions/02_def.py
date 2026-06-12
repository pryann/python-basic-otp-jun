def greetings(name: str) -> str:
    return f"Hi {name}!"


result = greetings("John")
print(result)
# greetings("Jane")
# greetings("Jack")


def calcualte_gross_price(net_price, vat_percent=27):
    return net_price * (1 + vat_percent / 100)


print(calcualte_gross_price(1000, 5))
print(calcualte_gross_price(10000))
print(calcualte_gross_price(1100))


def calcualte_full_price(net_price, vat_percent=27, discount_percent=0):
    return net_price * (1 + vat_percent / 100) * (1 - discount_percent / 100)


print(calcualte_full_price(1000))
print(calcualte_full_price(1000, discount_percent=10))
