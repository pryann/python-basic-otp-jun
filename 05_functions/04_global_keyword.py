full_price = 0


# def calcualte_full_price(net_price, vat_percent=27, discount_percent=0):
#     global full_price
#     full_price = net_price * (1 + vat_percent / 100) * (1 - discount_percent / 100)


# calcualte_full_price(1000)
# print(full_price)


def calcualte_full_price(net_price, vat_percent=27, discount_percent=0):
    return net_price * (1 + vat_percent / 100) * (1 - discount_percent / 100)


full_price = calcualte_full_price(1000)
