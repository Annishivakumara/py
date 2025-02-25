class Car:
    def __init__(self, name, year):
        self.Brandname = name
        self.year = year
        
    def displayInfo(self):
        print(f"This is a Car {self.Brandname}")
        print(f"The car Year is {self.year}")        

car1 = Car("Tesla", 2025) 

car1.displayInfo()
