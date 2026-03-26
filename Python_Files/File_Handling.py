

with open("Test File.txt", "r", encoding="utf-8") as file:
    print(file.read())

with open("Test File.txt", "a", encoding="utf-8") as f:
    text = input("Write what you want to add: ")
    f.write(text + "\n")

print("File Written Successfully")
print(">>>>>>>============================<<<<<<<<<")

with open("Test File.txt", "r", encoding="utf-8") as file:
    print(file.read())
    