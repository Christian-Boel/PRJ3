status = 0
with open("test.txt","r") as file:
    file.seek(0,2)
    file.seek(file.tell() - 1, 0)
    status = int(file.read())

print(status)

with open("test.txt", "a") as file:
    file.write("2")