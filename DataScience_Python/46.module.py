# WAP to create & import user defined module and use it 

import My_module as MD

a = int(input("Enter the side of square: "))
print(f"The area square is {MD.area(a)}")
print(f"The perimneter of the square is {MD.perimeter(a)}")

l = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
print(f"The area Rectangle is {MD.area2(l, b)}")
print(f"The perimneter of the Rectangle is {MD.perimeter2(l, b)}")

print(f"\nValue of PIE = {MD.PI}")
print(f"The factorial of 5 is {MD.factorial(5)}")

my_car = MD.Car("Red", 15000, 220)
print(my_car.start())
print(my_car.display_info())


# OUTPUT

# Enter the side of square: 4
# The area square is 16
# The perimneter of the square is 16
# Enter the length of rectangle: 2 
# Enter the breadth of the rectangle: 3
# The area Rectangle is 6
# The perimneter of the Rectangle is 10
# 
# Value of PIE = 3.141
# The factorial of 5 is 120
# The Red car with a top speed of 220 km/h is starting.
# Car Color: Red
# Milage: 15000 km
# Top Speed: 220 km/h