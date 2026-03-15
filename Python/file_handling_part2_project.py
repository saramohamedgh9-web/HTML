
with open("File_text.txt", "w") as f:
    f.write("Hello World!!")
f.close()


with open("File_text.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
file.close()


file = open('New Document.txt', 'x')
import os
if os.path.exists("demofile.txt"):
    print("File exists!!!")
else:
    print("The file does not exist")
file = open("my_doc.txt", "w")