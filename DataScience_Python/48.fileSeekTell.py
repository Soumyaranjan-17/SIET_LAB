#WAP to show the use of seek and tell 

myFile = open("myFile.txt", "w")

myFile.write("Jay Jagannath")
myFile.write("\nHare Krushna")
myFile.write("\nHare Rama")
myFile.close()

myFile = open("myFile.txt", "r")
print("Printing 1st 13 char")
print(myFile.read(13), "\n")

print("Printing again from 0th position using seek")
myFile.seek(0)
print(myFile.read())

print("Final position of the file pointer:" , myFile.tell())

myFile.close()

# OUTPUT
# Printing 1st 13 char
# Jay Jagannath 
# 
# Printing again from 0th position using seek
# Jay Jagannath
# Hare Krushna
# Hare Rama
# Final position of the file pointer: 36