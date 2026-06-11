# a = "a"
# b = "b"
# c = "c"
# variable definition
a, b, c = "a", "b", "c"
print(a, b, c)

# data swap
a = 10
b = 20

# tmp = a
# a = b
# b = tmp

a, b = b, a
print(a, b)


# unpack strings
# the number of characters and the number of ariables need to be equal
abc = "abc"
a, b, c = abc
print(a, b, c)

# unpack list
# user = ["John", "Doe", 33, ["reading"], "user"]
# first_name, last_name, age, *rest = user
# print(first_name, last_name, age, rest)

user = ["John", "Doe", 33, ["reading"], "user"]
first_name, *_, role = user
print(first_name, role)

# unpack matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Not pretty
# (a, b, c), (e, f, g), (h, i, j) = matrix
# print(a, b, c, e, f, g, h, i, j)
