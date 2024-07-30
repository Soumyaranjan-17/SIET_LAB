num = int(input("Entrer a number: "))

i = 2
while(i <= num/2):
    if(num % i == 0):
        print(f"{num} is Composite number")
        break
    i += 1
else:
    print(f"{num} is a prime number")


# Output
# Entrer a number: 45
# 45 is Composite number
# 
# Entrer a number: 13
# 13 is a prime number