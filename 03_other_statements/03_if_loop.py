yearly_salaries = [
    50_000,
    60_000,
    70_000,
    80_000,
    90_000,
    100_000,
]
high_salary_treshold = 75_000
sum_high_salaries = 0
sum_low_salaries = 0

for yearly_salary in yearly_salaries:
    if yearly_salary >= high_salary_treshold:
        sum_high_salaries += yearly_salary
    else:
        sum_low_salaries += yearly_salary

print(sum_high_salaries)
print(sum_low_salaries)
