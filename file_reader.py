#file_path="./pi_digits.txt"
file_path="../pythoncrashsamples/pcc/chapter_10/pi_million_digits.txt"
with open(file_path) as file_object:
    contents=file_object.read()
    #print(contents.rstrip())

print ("lets recreate pi number")
with open(file_path) as file_object:
    lines=file_object.readlines()

pi_string=''
for line in lines:
    pi_string +=line.strip()

print("pi number is:",pi_string[:52],"...") 
birthday=input("enter your birthday in format mmddyy:")   
if birthday in pi_string:
    print("your birthday is in first million digits of pi number")
else:    
    print("your birthday is not in first million digits of pi number")
