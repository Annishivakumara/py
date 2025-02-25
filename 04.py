#Experiment No : 4
#Name of the Experiment : Program to demonstrate Inner Classes and Passing Members 
#from one Class to another class

class Person:
    def __init__(self, name, age):
       self.name=name
       self.age=age
       self.db=self.Dob()
       
    def display(self):
       print(f"name Of The car:- {self.name} " )
       
       #this is inner class
    class Dob:
            def __init__(self):
               self.dd=10
               self.mm=5
               self.yy=2000
            
            def display(self):
                print(f"DOB:- {self.dd}/{self.mm}/{self.yy}")
               
             
#creating Person class object
name=input("Enter The Name of The Person:-")
age=int(input("Enter The Age Of The Person:-"))

p=Person(name,age)
p.display()

#creating Inner Calss Object

#x=p.db
x = p.db
x.display()

