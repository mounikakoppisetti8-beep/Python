class Car:
    def _init_(self,make,model,year):

       self.make = make 
       self.model = model
       self.year = year
       self.is_started = False
    
    def start(self):
        if not self.is_started:
            print("The{self.year}{self.make}{self.model} is starting.")
            self.is_started = True
        else:
            print("The{self.year}{self.make}{self.model} is already running.")

    def stop(self):
         if self.is_started:
             print("The{stop.year}{stop.make}{stop.model} is stopping.") 
         else:
             print("The {stop.year}{stop.make}{stop.model} is already stopped.") 
  
print("---Car Class Demonstration----")
my_car = Car("Toyota","Camry",2023)
print("My car:{my_car.make}{my_car.model}({my_car.year})")


my_car.start()
my_car.start()
my_car.stop()
my_car.stop()   