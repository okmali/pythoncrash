print("Lets divide. Press q to exit!")
cont=True
while cont:
    firstnum=int(input("first number:"))
    secondnum=int(input("second number:"))
    try:
        result=firstnum/secondnum
    except ZeroDivisionError:
        print("you cant divide by zero. Try Again")
    else:
        print ("the result is:",result)    
    cont=False if (input("continue?").lower()=='q') else True
