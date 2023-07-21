class Car:

    def __init__(self,n,c,s): # CONSTRUCTOR
        self.Name=n
        self.Color=c
        self.Speed=s
        
    def drive(self):
        print(self.Name, " is Driving")
        
    def gps(self):
        print(self.Name, " gps is working")
        
    def park(self):
        print(self.Name," is parked")
        
    def radio(self):
        print("Radio is Playing")
        

car1 = Car('x6','black',150) # Object Creation
car2 = Car('q3','red',200)

print(car1.Speed)
car1.park()

print(car2.Color)
car2.drive()

class truck (Car):

    pass
    def __init__(self, n, c, s,wheel):
        super().__init__(n, c, s)
        self.wheel=wheel
        
    def location(self):
        print(self.Name,"location is arrived")
    def wheel(self):
        print(self.wheel,"truck wheel is")
    def details(self):
        print(self.Name,self.Color,self.Speed,self.wheel)
    
    
truck1=truck("dous","gray",100,12)
truck1.drive()
truck1.gps()
truck1.location()
truck1.details()