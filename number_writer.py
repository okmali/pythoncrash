import json

number1={
        "num1":2,
        "num2":5,
        "num3":7,
        "num4":10,
        "num5":12
}

number2={
        "num1":2,
        "num2":5,
        "num3":7,
        "num4":10,
        "num5":12
}

myList=[number1,number2]
filename="./numbers.json"
with open(filename,'a') as file_obj:
    for num in myList:
        json.dump(num,file_obj)
    