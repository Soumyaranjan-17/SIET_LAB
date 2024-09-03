# WAP to declare a list and add eleemnt into it dynamically , sort it and display them

k = []

n = int(input("Enter the length : "))
for i in range(n):
    p = int(input("Enter value: "))
    k.append(p)

k.sort()
print(k)

# OUTPUT

# Enter the length : 5
# Enter value: 23
# Enter value: 56
# Enter value: 78
# Enter value: 34
# Enter value: 76
# [23, 34, 56, 76, 78]