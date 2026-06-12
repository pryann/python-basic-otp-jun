with open("text.txt", "r") as file:
    # read the whole file
    print(file.read())
    file.seek(0)
    # read one line
    print(file.readline())
    file.seek(0)
    # read line by line
    for line in file:
        print(line)
    file.seek(0)
    # read lines, and put them into a list
    print(file.readlines())
