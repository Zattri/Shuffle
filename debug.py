#------------------------------------------------------------------------
# Day 1
name = "Ollie"
age = 20
trueFalse = False

def ifTrue():    
    if (trueFalse == True):
        print("It is true")
    elif (trueFalse == False):
        print("It is not true")

def example(param1, param2):
    print(param1, param2)


#example_List = ["Ollie", "Sophie", "Tim", "Tilly"]

def forLoop():
    numbers = [3, 4, 5, 6]
    for x in numbers:
        print(x)

def printBox():
    print(" -----")
    print("|     |")
    print("|     |")
    print("|     |")
    print(" -----")

def printXBox(n):
    print(" " + "-" * n)
    for x in range(0,n):
        print("|" + " " * n + "|")
    print(" " + "-" * n)

#------------------------------------------------------------------------
# Day 2

def getInput():
    result = input("Prompt string ")
    print(result)


def calculator():
    firstNum = float(input("Input the first number "))
    opperator = input("Input the opperator ")
    secondNum = float(input("Input the second number "))

    if (opperator == "+"):
        answer = firstNum + secondNum
    elif (opperator == "-"):
        answer = firstNum - secondNum 
    elif (opperator == "*"):
        answer = firstNum * secondNum
    elif (opperator == "/"):
        answer = firstNum / secondNum
    else:
        error = "Incorrect opperator, please input +, -, *, or /"
        
    try:
        print(answer)
    except:
        print(error)

calculator()





