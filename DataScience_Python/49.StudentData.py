# WAP to access the name, branch and age of students and write to "StudentData.txt" and display it

studentData = open("studentData.txt", "a")

n = int(input("Enter the no of students: "))
for i in range(n):
    nm = input("Name: ")
    branch = input("Branch: ")
    age = input("Age: ")

    studentData.write("Name:"+ nm + '\n')
    studentData.write("Branch:" +branch + '\n')
    studentData.write("Age:" + age + '\n')

studentData.close()
studentData = open("studentData.txt", "r")
print(studentData.read())
studentData.close()


# OUTPUT
# Enter the no of students: 3
# Name: Soumya
# Branch: CSE
# Age: 20
# Name: Satya
# Branch: CIVIL
# Age: 21
# Name: Jagadish
# Branch: EE
# Age: 22
# Name:Soumya
# Branch:CSE
# Age:20
# Name:Satya
# Branch:CIVIL
# Age:21
# Name:Jagadish
# Branch:EE
# Age:22
# 

