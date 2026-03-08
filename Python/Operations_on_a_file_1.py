file = open("File_text.1", "r")  # Open the file in read mode
print(file.read())  # Read the contents of the file and print it
file.close()  # Close the file

file = open("File_text.1", "r")  # Open the file in read mode
print("n")
print(file.readline(8))  # Read the first line of the file and print it
file.close()  # Close the file

