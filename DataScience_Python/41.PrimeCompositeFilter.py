nums = [n for n in range(21)]

def isPRIME(n):
    if n < 2:
        return False
    
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def isCOMPOSITE(n):
    if n < 4:
        return False
    
    for i in range(2, n//2):
        if n % i == 0:
            return True
    return False

evenList = list(filter(isPRIME, nums))
oddList = list(filter(isCOMPOSITE, nums))

print(f"The prime List: {evenList}")
print(f"The composite list: {oddList}")

# OUTPUT 
# The prime List: [2, 3, 5, 7, 11, 13, 17, 19]
# The composite list: [6, 8, 9, 10, 12, 14, 15, 16, 18, 20]