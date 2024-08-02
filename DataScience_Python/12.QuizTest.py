print("WELCOME TO QUIZ TEST")
responce = input("Do you want to play(y/n)")
y_responce = ["Y", "y", "Yes", "yes", "YES"]
score = 0
if (responce in "Y y Yes yes YES"):
    print("...Ans in small case to avoid any error...\n...Good Luck...")

    ans =  input("1: Who discovered Python?")
    if (ans == "guido" or ans == "guido van rossam"):
        print("Correct")
        score+=1
    else:
        print("Wrong ans\nTry Next")
    

    ans =  input("2: In which year Python discovered?")
    if (ans == "1991"):
        print("Good Job")
        score+=1
    else:
        print("Wrong Ans\nTry Next")


    ans =  input("3: Is Python interpreted or compiled?")
    if (ans == "interpreted"):
        print("Good Job")
        score+=1
    else:
        print("Wrong Ans\nTry Next")
    
    
    ans =  input("4: What is the file extension for Python files?")
    if (ans == ".py"):
        print("Good Job")
        score+=1
    else:
        print("Wrong Ans\nTry Next")
    
    ans =  input("5: Which keyword is used to exit from a loop in Python?")
    if (ans == "break"):
        print("Good Job")
        score+=1
    else:
        print("Wrong Ans\nTry Next")
    
    ans =  input("6: Which keyword is used to define a conditional statement in Python?")
    if (ans == "if"):
        print("Good Job")
        score+=1
    else:
        print("Wrong Ans\nTry Next")
    
    ans =  input("7: What keyword we use to print a sentence in pytghon?")
    if (ans == "print"):
        print("Good Job")
        score+=1
    else:
        print("Wrong Ans\nTry Next")
    
    ans =  input("8: Which built-in function is used to get user input in Python?")
    if (ans == "input"):
        print("Good Job")
        score+=1
    else:
        print("Wrong Ans\nTry Next")
    
    ans =  input("9: Which operator is used for integer division in Python?")
    if (ans == "//"):
        print("Good Job")
        score+=1
    else:
        print("Wrong Ans\nTry Next")
    
    
        
    ans =  input("10: Which module is used for mathematical operations in Python?")
    if (ans == "math"):
        print("Good Job")
        score+=1
    else:
        print("Wrong Ans\n You have completed the quiz")
    
    print(f"Your score is {score}.")
    print("You got stars")
    for i in range(score):
        print("⭐")