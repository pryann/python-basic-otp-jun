# unordered
# unindexed
# not contains duplicated elements

numbers = {1, 2, 3}
print(numbers, type(numbers))

numbers.add(4)
print(numbers)

numbers.update([3, 4, 5, 6])
print(numbers)

# remove: raise error if the value not exists
# numbers.remove(30)
# print(numbers)

numbers.discard(1)
print(numbers)

numbers.pop()
print(numbers)

x1 = {"a", "b", "c"}
x2 = {"b", "c", "d"}

print(x1.union(x2))
print(x1.intersection(x2))
print(x1.difference(x2))
print(x1.symmetric_difference(x2))
print({"b"}.isdisjoint(x2))
print(x1.issubset({"a", "b", "c", "d"}))
print(x1.issuperset({"a", "b"}))

non_unique_values = [1, 2, 3, 4, 5, 6, 2, 2, 3, 4, 4, 1]
unique_values = list(set(non_unique_values))
print(unique_values)
