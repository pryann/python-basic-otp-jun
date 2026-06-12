def add_item_to_basket(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


# print(add_item_to_basket("Apple", ["Orange"]))
# print(add_item_to_basket("Banana", ["Pinnacle"]))

print(add_item_to_basket("Apple"))
print(add_item_to_basket("Banana"))
print(add_item_to_basket("Orange"))
