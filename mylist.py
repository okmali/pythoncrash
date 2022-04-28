motorbikes=[]
motorbikes=['ducati','yamaha','honda','aprilia']
motorbikes.sort(reverse=True)
print("sorted list:",motorbikes)
poppedmotorbike=motorbikes.pop()
print("poped last motorbike:",poppedmotorbike)
print("motorbike list:",motorbikes)
poppedmotorbike=motorbikes.pop(0)
print("popped first motorbike:",poppedmotorbike)
print("motorbike list:",motorbikes)

print("*************")
motorbikes=['ducati','yamaha','honda','aprilia']
print("sorted bikes:",sorted(motorbikes))
print("reverse sorted bikes:",sorted(motorbikes,reverse=True))
expensive='ducati'
motorbikes.remove(expensive)
print(motorbikes)

for motorbike in motorbikes:
    print(motorbike.title())

for value in range(1,6):
    print (value)

numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(0,11,2))
print("even numbers:",even_numbers)
