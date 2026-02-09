# File write
with open("data.txt", "w") as f:
    f.write("Python is easy\n")
    f.write("I am learning Python\n")

# File read
with open("data.txt") as f:
    print(f.read())

# Append data
with open("data.txt", "a") as f:
    f.write("I am appending this line\n")

# Line by line read
with open("data.txt") as f:
    for line in f:
        print(line.strip())

