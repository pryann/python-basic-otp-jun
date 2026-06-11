prog_lang = "Java"

# A   B   A or B
# 0   0     0
# 0   1     1
# 1   0     1
# 1   1     1

# Not use this type, if you have only one variable
# if prog_lang == "Java" or prog_lang == "Python":
#     print("Backend language")

backend_language = ["Java", "Python"]

if prog_lang in backend_language:
    print("Backend language")


age = 7

# A   B   A and B
# 0   0     0
# 0   1     0
# 1   0     0
# 1   1     1

if age < 18:
    print("kiskorú")
# elif 18 <= age < 65:
elif age >= 18 and age < 65:
    print("felnőtt")
else:
    print("nyugdíjas")


temperature = 50
humidity = 60
rain = True

if temperature > 30 or humidity < 70 and not rain:
    print("Dry weather")

# not rain -> False
# humidity < 70 ->True
# False and True -> False
# temperature > 30 -> True
# False or True -> True

if (temperature > 30 or humidity < 70) and not rain:
    print("Dry weather")

# humidity < 70 ->True
# temperature > 30 -> True
# True or True -> True
# not rain -> False
# False and True -> False
