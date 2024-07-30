a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))

if(a > b):
    if(a > c):
        print(f"{a} is greatest")
    else:
        print(f"{c} is greatest")
else:
    if(b > c):
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")