#Experiment No : 7
#Name of the Experiment : Demonstrate a Python program using a class called Car that 
#includes attributes for make, model, mileage, and price. The program should include 
#methods to display the car's details, start and stop the car, and update its price. Provide an 
#example of creating two car objects and calling their methods

class Car:
    
    def __init__(self,make,model,milage,price):
        self.make=make
        self.model=model
        self.milage=milage
        self.price=price
        self.isrunning=False
        
    def display(self):
        print("Making",self.make)
        print("Model",self.model)
        print("Milage",self.milage)
        print("Price",self.price)
        
    def start(self):
        if not self.isrunning:
            self.isrunning=True
            print("Car is STarted")
            
    def stop(self):
        if self.isrunning:
            self.isrunning=False
            print("car Stopped")
    
    def update_price(self,new_price):
        self.price=new_price
        print("price Updated")
        
carname=input("Enter The car Name ")
model=input("Enter The Mdoel ")
milage=int(input("Enter The Milage"))
price=int(input("Enter The Price Of The Car"))

car1=Car(carname,model,milage,price)
car1.display()
