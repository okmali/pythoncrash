class Dog():
    """A simple attempt to model a dog"""

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(self.name,'is sitting now!')
 
    def roll_over(self):
        print(self.name,'is rolling over now')


mydog=Dog(name='loki',age=20)
mydog.sit()
print('My Dog''s name is', mydog.name)
