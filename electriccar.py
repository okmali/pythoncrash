from car import Car,Battery

class ElectricCar(Car):
    def __init__(self,make,model,year,batterysize=70):
        super().__init__(make,model,year)
        self.battery=Battery(batterysize)