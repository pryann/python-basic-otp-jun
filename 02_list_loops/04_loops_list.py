yearly_salaries = [120_000, 92_000, 75_000, 210_000]

for yearly_salary in yearly_salaries:
    print(yearly_salary)

for i in range(len(yearly_salaries)):
    print(f"index: {i}, value: {yearly_salaries[i]}")

for index, value in enumerate(yearly_salaries):
    print(f"index: {index}, value: {value}")
