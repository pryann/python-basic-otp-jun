# not typed
# can contains duplicated items
# ordered
# mutable
yearly_salaries = [100_000, 110_000, 120_000, 90_000, 90_000, "nulla"]
print(yearly_salaries, type(yearly_salaries))

print(yearly_salaries[0])
# IndexError: list index out of range
# print(yearly_salaries[10])

print(len(yearly_salaries))

# concat
print([1, 2, 3] + [4, 5, 6])
# multiplication
print([1, 2, 3] * 3)

# MUTABLE
print(id(yearly_salaries))
yearly_salaries[0] = 0
print(id(yearly_salaries))
print(yearly_salaries)

# delete by index
del yearly_salaries[1]
print(yearly_salaries)


# methods
# append one item to the end
yearly_salaries.append(1_000_000)
print(yearly_salaries)

# add elements to the end
yearly_salaries.extend([1, 2, 3])
print(yearly_salaries)

# append to a specific place (index)
yearly_salaries.insert(0, "inserted item")
print(yearly_salaries)

# remove by value, first apperance
yearly_salaries.remove("inserted item")
print(yearly_salaries)

# remove an element by index, default the last element
yearly_salaries.pop()
print(yearly_salaries)

# count the value
print(yearly_salaries.count(90_000))

yearly_salaries = [3, 4, 6, 1, 2, 8]
yearly_salaries.sort(reverse=True)
print(yearly_salaries)

yearly_salaries.reverse()
print(yearly_salaries)

# str method, use list
user = ["My", "name", "is", "John", "Doe", "."]
print("-".join(user))
