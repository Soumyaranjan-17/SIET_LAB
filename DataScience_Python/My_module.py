PI = 3.141

def area(a):
    return a*a

def area(l,b):
    return l*b

def perimeter(a):
    return 4*a

def perimeter(l,b):
    return 2*(l+b)

def vol(a):
    return a*a*a

def vol(l, b, h):
    return l*b*h

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

class Car:
    color = "Transparent"
    milage = 0
    top_speed = 0
    def __init__(self, color, milage, top_speed) -> None:
        self.color = color
        self.milage = milage
        self.top_speed = top_speed

    def start(self):
        print(f"This {self.color} car is starting")
        