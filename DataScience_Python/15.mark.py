# WAP to ijnput name , 5 different mark and find grade and percentage with name

name = input("Enter your name: ")
m1 = int(input("Enter Mark 1: "))
m2 = int(input("Enter Mark 2: "))
m3 = int(input("Enter Mark 3: "))
m4 = int(input("Enter Mark 4: "))
m5 = int(input("Enter Mark 5: "))


total_marks = m1 + m2 + m3 + m4 + m5
percentage = (total_marks/500)*100

if percentage >= 90:
    grade = "O"
elif percentage >= 80:
    grade = "E"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
elif percentage >= 30:
    grade = "E"
else:
    grade = "F"

print(f"Name: {name}")
print(f"Total mark: {total_marks}")
print(f"Grade: {grade}")
