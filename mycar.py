#import car
from car import Car
from electriccar import ElectricCar

mycar=Car('Nissan','Qashqai',2016)
mycar.set_adometer(87000)
myECar=ElectricCar('Tesla','Super X',2022,100)

print(mycar.get_descriptive_name())
print(myECar.get_descriptive_name())
print("My ECar:",myECar.battery.get_battery_info())
print("My ECar's range is:",myECar.battery.get_battery_range())
