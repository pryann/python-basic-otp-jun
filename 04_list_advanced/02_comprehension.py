net_prices = [1000, 2000, 10_000, 99_000]
vat_percent = 27

# gross_prices = []
# for i in net_prices:
#     gross_prices.append(i * (1 + vat_percent / 100))

gross_prices = [i * (1 + vat_percent / 100) for i in net_prices]

print(gross_prices)

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grades = [i for i in values if 0 < i < 6]
print(grades)
even = [i for i in values if i % 2 == 0]
odd = [i for i in values if i % 2 != 0]
print(even)
print(odd)

matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

flatten_matrix = [j for i in matrix for j in i]
print(flatten_matrix)
