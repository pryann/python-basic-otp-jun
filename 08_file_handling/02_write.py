# w: overwrite the content
# create file if not exists
with open("new_file.txt", "w") as file:
    file.write("content2\n")

content = ["line 1\n", "line 2\n", "line 3"]

# append to the end
with open("new_file.txt", "a") as file:
    file.writelines(content)

content = ["line", "line", "line"]
with open("new.txt", "w") as f:
    f.write("\n".join(content))


with open("text.txt", "r+") as f:
    content = f.read()
    f.seek(0)
    f.write(content.replace("line", "LINE"))
