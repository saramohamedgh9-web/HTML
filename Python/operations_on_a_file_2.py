with open("File_text.txt", "w") as file:
    file.write("I am a 1 year old penguin.")

with open("File_text.txt", "r") as file:
    data = file.readlines()
    print("Words in this file are: ")
    for line in data:
        words = line.split()
        for word in words:
            print(word)
