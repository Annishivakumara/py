#Experiment No : 3
#Name of the Experiment : Program to demonstrate Class Methods, Instance Methods 
#and Static Methods

class car:
    wheels=int(input("Enter The Car Wheels:-"))
    def __init__(self, brandname, year):
        self.brandname=brandname
        self.year=year
        
    def display_info(self):
        print(f"This is The Car:- {self.brandname} ")
        print(f"This the year :- {self.year}")
    
    # Class method (takes 'cls' as the first argument)
    @classmethod
    def changewheels(cls,new_wheels):
        cls.wheels=new_wheels
        print(f"Number of Wheels in the car:- {car.wheels}")
        
   # Static method (doesn't take 'self' or 'cls' as the first argument)
    @staticmethod
    def it_is_a_ecoFriendly(brand):
        if brand=="Tesla":
            print("Eco Friendly car")
        else:
            print("It's Not a Eco Friendly car ")
        
name=input("Enter The Car  Name:- ")
year=int(input("Enter The Year of the  car :- "))
car1=car(name, year)
car1.display_info()       

car1.changewheels(4)
car1.it_is_a_ecoFriendly(name)