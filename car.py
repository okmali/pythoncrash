class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.adometer=0
    
    
    def increment_adometer(self,increment):
        if increment<0:
            print('You can''t increase adometer!!')    
        else:
            self.adometer += increment
    
    
    def set_adometer(self,reading):
        if reading < self.adometer:
            print('You can''t increase adometer!!')
        else:
            self.adometer=reading


    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model+' at '+str(self.adometer) +' KM'
        return long_name


class Battery():
    def __init__(self,batterysize):
        self.batterysize=batterysize
   
    
    def get_battery_info(self):
        return ('This is a'+' '+ str(self.batterysize)+' KWH Battery')

    def get_battery_range(self):
        if self.batterysize==70:
            return 240
        elif self.batterysize==80:
            return 270
        else:
            return 300