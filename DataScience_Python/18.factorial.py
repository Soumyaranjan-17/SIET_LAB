n = int(input("Enter a number to find factorial: "))
fact = 1
while(n > 0):
    fact = fact * n
    n -= 1
print("Factorial is: ", fact)