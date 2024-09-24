nums = [1,2,3,4,5,6,7,8,9,10]

def isEVEN(n):
    return n % 2 == 0

def isODD(n):
    return n % 2 == 1
evenList = list(filter(isEVEN, nums))
oddList = list(filter(isODD, nums))

print(evenList)
print(oddList)