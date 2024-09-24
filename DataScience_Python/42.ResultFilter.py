# WAP to create a dictionary containing roll no as key and percentage of mark. Filter the roll numbers of those student achive more than 70, 80, 90 percentage.


marks = {
    1: 73,
    2: 51,
    3: 80,
    4: 65,
    5: 44,
    6: 98,
    7: 92,
    8: 59,
    9: 24,
    10: 31,
    11: 28,
    12: 17,
    13: 32,
    14: 22,
    15: 17,
    16: 25,
    17: 79,
    18: 21,
    19: 3,
    20: 13
}

def AGrade(roll):
    if (marks[roll] >= 90):
        return True
    return False

def BGrade(roll):
    if (marks[roll] >= 80):
        return True
    return False

def CGrade(roll):
    if (marks[roll] >= 70):
        return True
    return False

A = list(filter(AGrade, marks))
B = list(filter(BGrade, marks))
C = list(filter(CGrade, marks))

print("Above 90: ")
print(A)
print("Above 80: ")
print(B)
print("Above 70: ")
print(C)

# OUTPUT

# Above 90: 
# [6, 7]
# Above 80: 
# [3, 6, 7]
# Above 70: 
# [1, 3, 6, 7, 17]