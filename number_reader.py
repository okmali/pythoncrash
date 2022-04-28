import json


filename="./numbers.json"
numbers=[]
with open(filename,'r') as file_obj:
    numbers=file_obj.readlines()
print(numbers[0])

print(json.JSONEncoder().encode(numbers[0]))    
    