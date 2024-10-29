#WAP to create a file named myFile.txt to write and read a message to it

myFile = open("myFile.txt", "w")

myFile.write("Jay Jagannath")
myFile.write("\nHare Krushna")
myFile.close()

myFile = open("myFile.txt", "r")
print(myFile.read())

myFile.close()

# OUTPUT
# Jay Jagannath
# Hare Krushna