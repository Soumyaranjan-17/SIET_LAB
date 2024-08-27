#WAP to perform area of a square , area of a rectangle, volume of cube, prime or composite, even or odd using functon, call according to your choise

def squa_area(a):
    return a**2
def rect_area(l, b):
    return l*b
def cube_vol(l, b, h):
    return l*b*h
def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while(i <= n/2):
        if (n % i == 0):
            return False
        i += 1
    return True
def isEven(n):
    return n % 2 == 0

# User Input
while(1):
    print("Choose an operation:")
    print("1. Area of Square")
    print("2. Area of Rectangle")
    print("3. Volume of Cube")
    print("4. Check if a number is Prime")
    print("5. Check if a number is Even")
    print("6. Exit")
    ch = int(input("Enter your ch: "))
    if ch == 6:
        break

    if ch == 1:
        s = float(input("Enter the side of square: "))
        print("Area of square is: ", squa_area(s))
    elif ch == 2:
        l = float(input("Enter the length of rectangle: "))
        b = float(input("Enter the breadth of rectangle: "))
        print("Area of rectangle is: ", rect_area(l, b))
    elif ch == 3:
        l = float(input("Enter the length of cube: "))
        b = float(input("Enter the breadth of cube: "))
        height = float(input("Enter the height of cube: "))
        print("Volume of cube is: ", cube_vol(l, b, height))
    
    elif ch == 4:
        num = int(input("Enter a number: "))
        if isPrime(num):
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")
    
    elif ch == 5:
        num = int(input("Enter a number: "))
        if isEven(num):
            print(num, "is an even number.")
        else:
            print(num, "is an odd number.")

    else:
        print("Invalid ch!")
