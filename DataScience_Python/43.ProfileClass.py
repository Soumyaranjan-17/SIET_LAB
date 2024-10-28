# WAP to access your profile and display them

class Profile:
    nm = ''
    roll = ''
    age = ''

    def __init__(self, name, roll, age) -> None:
        self.nm = name
        self.roll = roll
        self.age = age
    
    def display(self):
        print("Your Name: ", self.nm)
        print("Your Roll No: ", self.roll)
        print("Your Age: ", self.age)

obj = Profile("Soumya", "CS-23-59", 19)
obj.display()

# OUTPUT

# Your Name:  Soumya
# Your Roll No:  CS-23-59
# Your Age:  19