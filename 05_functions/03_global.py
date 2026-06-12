global_var = "global"


def calcualte_full_price(net_price, vat_percent=27, discount_percent=0):
    print(global_var)
    full_price = net_price * (1 + vat_percent / 100) * (1 - discount_percent / 100)
    return full_price


print(global_var)
fp = calcualte_full_price(1000)
print(fp)
# NameError: name 'full_price' is not defined
# print(full_price)
