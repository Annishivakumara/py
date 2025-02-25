#Experiment No : 5
#Name of the Experiment : Demonstrate the functionality of the Bank class by creating 
#an instance of the class (name,accno,phno), and showcase how to access its public, private, 
#and protected attributes

class Bank:
    
    #public Access Specifier
    def __init__(self, name, accno,phno):
        self.name=name
        self.accno=accno
        self.phno=phno
        self._balance=1000  #Protected attribute (by convention)
        self.__pin=1234    #private Attiribuet
        
     # Method to deposit money (updates the protected attribute)
    def deposit(self,ammount):
        if(ammount>0):
            self._balance+=ammount
            print("Amount Deposited:-",ammount)
            
    #Method To withdraw The Money 
    def withdraw(self, ammount):
        if ammount<0:
            print("amount Should be Greater Than 1")
        elif ammount>self._balance:
            print("Insufficient Balance") 
        else:
            self._balance-=ammount
            print("Amount Withdrawn:-",ammount)
                     
    def setnewpin(self, newpin):
        self.__pin=newpin
        print("Pin CHanges SuccessFully")
        
    def getpin(self):
        return self.__pin
    
    # Method to display information (demonstrating public and protected attributes)
    def diplay(self):
        print(f"Name:-{self.name}")
        print(f"Account Number:-{self.accno}")
        print(f"Phone Number:- {self.phno}")
        print(f"Balance:-{self._balance}")
        

# Creating an instance of the Bank class
name=input("Enter The Name:-")
accno=int(input("Enter The Account Number:-"))
phno=int(input("Enter The Phone Number:-"))

customer=Bank(name, accno,phno)

#Public Attributes
print("Public Attributes:-",customer.name)
print("Public Attributes:-",customer.accno)
print("Public Attributes:-",customer.phno)



# Accessing private attribute using a method
# set a Pin
customer.setnewpin(5678)
print("Private Attributes Using Method:-",customer.getpin())

# Demonstrating deposit method and updated balance
customer.deposit(500)
customer.withdraw(200)
customer.diplay()