import mathematical as my_math
import math as std_math
# from package import module

# print(module.summa(1, 2))
from package.module import summa

print(summa(1, 2))

print(my_math.PI)
print(std_math.pi)
