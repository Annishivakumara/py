class car:
    wheels=int(input("Enter The Wheels:-"))
    def __init__(self,brandname, year):
        self.brandname=brandname
        self.year=year
        
    def displayinfo(self):
        print(f"This is car : {self.brandname}")
        print(f"this is the  Year Car Lounched: {self.year}")
        print(f"Number of Wheerls in the car: {self.wheels}")
   

name=input("Enter The of The Car: ")
year=int(input("Enter The Year of the Car :-"))
car1=car(name,year)     
car1.displayinfo()
car.wheels=int(input("Enter  The Car Wheels"))

print(f"After The Car Modifying in guarge the wheels are {car.wheels}")