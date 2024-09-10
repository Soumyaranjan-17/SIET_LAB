# WAP to create a stack of given size and perform push and pop operation using list 
def add(STACK, Element):
    if(len(STACK) == 5):
        print("Can not Overflow\nAborting...")

    STACK.append(Element)
    print("")

def pop(STACK):
    print(f"Deleted {STACK.pop()}")

SIZE = 5
stack = []

while 1:
    print("1. Add element to Stack.\n2. Delete an element from the stack.\n3. Exit ")
    ch = int(input("Choose Option: "))
    
    if ch == 1:
        n = int(input("Enter a Number: "))
        add(stack, n)
    
    elif ch == 2:
        pop(stack)
    
    elif ch == 3:
        exit()
    
    else:
        print("Choose a Valid Option.")