# like an immutable list
# ordered
# indexed
# allow duplicate members
# allow any types of data


yearly_salaries = (10_000, 20_000, 30_000)

print(yearly_salaries.index(10_000))
print(yearly_salaries.count(10_000))

print(yearly_salaries[0])
# TypeError: 'tuple' object does not support item assignment
# yearly_salaries[0] = 100000
# yearly_salaries = 10
# print(yearly_salaries)

rgb = (255, 255, 10)
location = (45.1234, 120.2345)

# IMMUTABLE, DO NOT DO THIS
rgb_list = list(rgb)
rgb_list[0] = 100
rgb = tuple(rgb_list)
print(rgb)

print(rgb[0:2])

r, g, b = rgb
print(r, g, b)

# fmt: off
one_item = (1)
print(type(one_item))

one_item = (1,)
print(type(one_item))

def statistics(numbers):
  return min(numbers), max(numbers)

numbers = [1,2,3,4,5,6]
result = statistics(numbers)
print(result, type(result))
