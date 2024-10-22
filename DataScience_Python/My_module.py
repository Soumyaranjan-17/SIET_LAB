PI = 3.141

def area(a):
    return a*a

def area2(l,b):
    return l*b

def perimeter(a):
    return 4*a

def perimeter2(l,b):
    return 2*(l+b)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

class Car:
    color = "Transparent"
    milage = 0
    top_speed = 0

    def __init__(self, color: str, milage: float, top_speed: float) -> None:
        self.color = color
        self.milage = milage
        self.top_speed = top_speed

    def start(self) -> str:
        return f"The {self.color} car with a top speed of {self.top_speed} km/h is starting."

    def display_info(self) -> str:
        return (f"Car Color: {self.color}\n"
                f"Milage: {self.milage} km\n"
                f"Top Speed: {self.top_speed} km/h")