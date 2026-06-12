from wsgiref import validate


user = {
    "name": "John Doe",
    "age": 33,
}

print(user["name"])
print(user["age"])

user["age"] = 44
print(user)

user["hobbies"] = ["reading", "listening music"]
print(user)

user.pop("hobbies")
print(user)

user.update({"age": 18, "hobbies": ["drawing"]})
print(user)

print(user.keys())
print(user.values())
print(user.items())

# i is keys
for i in user:
    print(i)

for i in user.values():
    print(i)

for key, value in user.items():
    print(key, value)
