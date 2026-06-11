# fmt: off
print('banana', type('banana'))
print("banana", type("banana"))
print('I\'m Gergő')
print("I'm Gergő")
# multiple, but the triple qoute used as docstring
print('''First line 
Second line''')
print('First line\nSecond line')

# fmt: on
first_name = "Gergely"
last_name = "Gáll"
age = 42
sentence = "My name is " + first_name + " " + last_name + ". I'm " + str(age) + " years old."
print(sentence)
sentence = "My name is {0} {1}. I'm {2} years old.".format(first_name, last_name, age)
print(sentence)
sentence = f"My name is {first_name} {last_name}. I'm {age} years old."
print(sentence)
