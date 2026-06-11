matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix[1][1])

for row in matrix:
    for item in row:
        print(item)


new_matrix = []
start_value = 1

for _ in range(3):
    row = []
    for _ in range(3):
        row.append(start_value)
        start_value += 1
    new_matrix.append(row)

print(new_matrix)
