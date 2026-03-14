file = open('File_text.txt', 'r')

print(file.read(12))

print(file.readline())

print(file.readlines())

for x in file:
    print(x)

file.close()