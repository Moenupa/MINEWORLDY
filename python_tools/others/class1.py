class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.type = 'Gasoline'
        self.oil_consume = 10
    def get_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print('this car has '+str(self.odometer_reading)+' miles on it.')
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back an odometer.')
    def get_type(self):
        return self.type
    def update_type(self,current_type):
        self.type = current_type
    def run_mile(self,mile):
        self.mile = mile
    def get_max_range(self)
    def update_oil_consume(self,consume):
        self.oil_consume = consume
    def get_oil

class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
        self.current = battery_size
    def get_battery_size(self):
        return self.battery_size
    def describe_battery_size(self):
        print('This car has a '+str(self.battery_size)+'-kWh battery.')
    def get_max_range(self):
        super().get_max_range(self)
        return self.battery_size*2+100
    def get_range(self,miles):
        self.current = (self.get_max_range - miles)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        self.type = 'Electric'
    def run_mile(self,miles):
        self.mile = miles
    def read_battery(self):
        try:
            self
        self.battery = self.mile

        
        
