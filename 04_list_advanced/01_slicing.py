from numpy import number


numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]

print(numbers[0])
print(numbers[2])

print("to the 2.:", numbers[:2])
print("from the 2.:", numbers[2:])
print("from the 2. to the 4.:", numbers[2:4])
print("from the 2. to the 8. step 2: ", numbers[2:8:2])
print("all step 2: ", numbers[::2])
print("last element: ", numbers[-1])
print("second last element: ", numbers[-2])
print("reverse: ", numbers[::-1])  # .reverse()

# .copy()
numbers_copy = numbers[:]
