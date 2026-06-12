import random
import os
from datetime import datetime, date, time
import subprocess

num = random.randint(1, 100)
print(num)

nums = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(nums)
print(nums)

pick = random.choice(nums)
print(pick)

print(datetime.now())
print(datetime(2020, 10, 10))
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print(datetime(2020, 10, 10).strftime("%Y %B %d."))
print(datetime(2020, 10, 10).isoformat())
print((datetime(2020, 10, 10, 10) - datetime(2020, 9, 9)).days)

d = date(2020, 7, 14)
print(d)
t = time(10, 11, 22, 123)
print(t)
print(datetime.combine(d, t))

print(datetime.now() - datetime(2020, 1, 1))
now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)

# os.mkdir("new_folder")
# os.rename("new_folder", "renamed_folder")
# os.rmdir("renamed_folder")
print(os.getcwd())
print(os.listdir())
print(os.cpu_count())
