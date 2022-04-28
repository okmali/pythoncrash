current_number=0
while current_number <=5:
    print("number:",current_number)
    current_number +=1

msg=""
while msg.lower() !='quit':
    msg=input("what? ")
    print("what:",msg)

while True:
    city=input("Which city would you like to visit? ")
    if city.strip().lower()=='quit':
        break
    else:
        print("I'd also like to visit",city, "!!")
