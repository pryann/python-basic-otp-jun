# IMMUTABLE

age = 18
age_copy = age

print(age, id(age))
print(age_copy, id(age_copy))

age = 42
print(age, id(age))
print(age_copy, id(age_copy))

# --------
# 18        <----- age = 18
#           <----- age_copy = age
# --------


# --------
# 42            <----- age = 42
# ---------
# 18            <----- age_copy
# --------

numbers = [1, 2, 3]
numbers_copy = numbers

print(numbers, id(numbers))
print(numbers_copy, id(numbers_copy))

numbers.append(4)
print(numbers, id(numbers))
print(numbers_copy, id(numbers_copy))
numbers_copy.append(5)
print(numbers, id(numbers))
print(numbers_copy, id(numbers_copy))

numbers = [10, 11, 12]
print(numbers, id(numbers))
print(numbers_copy, id(numbers_copy))

numbers_copy = numbers.copy()
print(numbers, id(numbers))
print(numbers_copy, id(numbers_copy))

print(10 in numbers)
