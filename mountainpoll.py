from collections import OrderedDict
#responses=OrderedDict()
responses={}
active=True
while active:
    name=input("What is your name:")
    mountain=input("which mountain would you like to climb " + name +"? ") 
    responses[name]=mountain
    active=False if input("Continue (yes/no)?").lower()!='yes' else True

print(responses)
