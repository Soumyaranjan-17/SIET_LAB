# WAP to copy the content of the existing file into another file in python

EXfile = open("studentData.txt", 'r')
content = EXfile.read()
EXfile.close()

print("Coping....")
newFile = open("EXfileCopy.py", 'w')
newFile.write(content)
newFile.close()

newFile = open("EXfileCopy.py", 'r')
print("Data inside new file\n" + newFile.read())
newFile.close()