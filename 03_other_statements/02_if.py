yearly_salary = 100_000
high_salary_treshold = 100_000

if yearly_salary > high_salary_treshold:
    print("High salary")
else:
    print("Low salary")

# in a real app, you need to validatate data, or use as string
# if grade.isdigit() and 0 < int(grade) < 6:
#     ...
grade = int(input("Adj meg egy osztályzatot (1-5): "))

# < > <= >= != ==
if grade == 1:
    print("Elégtelen")
elif grade == 2:
    print("Elégséges")
elif grade == 3:
    print("Közepes")
elif grade == 4:
    print("Jó")
elif grade == 5:
    print("Jeles")
else:
    print("Ez nem érdemjegy")
