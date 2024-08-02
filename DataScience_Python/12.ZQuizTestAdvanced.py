print("WELCOME TO QUIZ TEST")
responce = input("Do you want to play?\nAns: ")

score = 0
if (responce in "Y y Yes yes YES"):
    print("...Ans in small case to avoid any error...\n......Good Luck......")

    ans =  input("1: Who discovered Python?\nAns: ")
    if (ans == "guido" or ans == "guido van rossam"):
        print("Correct ✅")
        score+=1
    else:
        print("Wrong ans ❌\nTry Next 👇")
    

    ans =  input("2: In which year Python discovered?\nAns: ")
    if (ans == "1991"):
        print("Correct ✅")
        score+=1
    else:
        print("Wrong Ans ❌\nTry Next 👇")


    ans =  input("3: Is Python interpreted or compiled?\nAns: ")
    if (ans == "interpreted"):
        print("Correct ✅")
        score+=1
    else:
        print("Wrong Ans ❌\nTry Next 👇")
    
    
    ans =  input("4: What is the file extension for Python files?\nAns: ")
    if (ans == ".py"):
        print("Correct ✅")
        score+=1
    else:
        print("Wrong Ans ❌\nTry Next 👇")
    
    ans =  input("5: Which keyword is used to exit from a loop in Python?\nAns: ")
    if (ans == "break"):
        print("Correct ✅")
        score+=1
    else:
        print("Wrong Ans ❌\nTry Next 👇")
    
    ans =  input("6: Which keyword is used to define a conditional statement in Python?\nAns: ")
    if (ans == "if"):
        print("Correct ✅")
        score+=1
    else:
        print("Wrong Ans ❌\nTry Next 👇")
    
    ans =  input("7: What keyword we use to print a sentence in python?\nAns: ")
    if (ans == "print"):
        print("Correct ✅")
        score+=1
    else:
        print("Wrong Ans ❌\nTry Next 👇")
    
    ans =  input("8: Which built-in function is used to get user input in Python?\nAns: ")
    if (ans == "input"):
        print("Correct ✅")
        score+=1
    else:
        print("Wrong Ans ❌\nTry Next 👇")
    
    ans =  input("9: Which operator is used for integer division in Python?\nAns: ")
    if (ans == "//"):
        print("Correct ✅")
        score+=1
    else:
        print("Wrong Ans ❌\nTry Next 👇")
    
    
        
    ans =  input("10: Which module is used for mathematical operations in Python?\nAns: ")
    if (ans == "math"):
        print("Correct ✅")
        score+=1
    else:
        print("Wrong Ans ❌\n You have completed the quiz")

    print(f"You scored {score} points.")
    if(score < 4):
        print("Not so Good\n⭐⚝⚝⚝⚝")
    elif(score < 7):
        print("Good Job\n⭐⭐⚝⚝⚝")
    elif(score < 10):
        print("You did well\n⭐⭐⭐⚝⚝")
    elif(score == 10):
        print("Excelent\n⭐⭐⭐⭐⭐")

    print("Thank U...")
    
else:
    print("💀")