squares=[]
for value in range(0,11,2):
    squares.append(value**2)
print("square list:",squares) 
print("min in the list:",min(squares)) 
print("max in the list:",max(squares)) 
print("sum of the list:",sum(squares)) 

cubicList=[value**3 for value in range(0,21,3)]
print ("cubic list:",cubicList)
print ("slicing the cubic list:",cubicList[3:6])
print ("another slice from the cubic list:",cubicList[:6])
print ("slice from the end of cubic list:",cubicList[-3:])

my_food=["pizza","hamburger","brocoli"]
friend_food=my_food[:]
my_food.append("spinach")
friend_food.append("carrot")
print("my food list:",my_food)
print("friend's food list:",friend_food)