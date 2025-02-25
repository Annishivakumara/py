#Experiment No : 6
#Name of the Experiment : Demonstrate a mini project Bank Account class(All attributes 
#should be private) to simulate basic banking operations such as depositing money, 
#withdrawing money, checking account balance, and displaying account details. Create an 
#instance of the class with initial values and demonstrate each of these operations.
class Bank:
    
    def __init__(self, name, accno, phno):
        self.__name=name
        self.__accno=accno
        self.__phno=phno
        self.__balance=1000
        self.__pin=1234
        
    def Deposit(self,amount):
            if amount<0:
                print("Amount Should be Greater Than 0")
            else:
                self.__balance+=amount
                print("Amount Deposited succesfully",amount)
                
    def withdraw(self, amount):
            if(amount<0):
                print("Amount Should Be Greater Than 0")
            elif amount>self.__balance:
                print("Insufficient Balance")
            else:
                self.__balance-=amount
                print("Amount Withdrawn Successfully", amount)
                
    def setnewpin(self, newpin):
        self.__pin=newpin
        print("Pin Changed Successfully")
    def getnewpin(self):
        return self.__pin
    
    def display(self):
        print(f"Name:-{self.__name}")
        print(f"Account Number:-{self.__accno}")
        print(f"Phone Number:-{self.__phno}")
        print(f"Balance:-{self.__balance}")
        print(f"pin:-{self.__pin}")
        
# Creating an instance of BankAccount
name=input("Enter The Name:-")
accno=int(input("Enter The Account Number:-"))
phno=int(input("Enter The Phone Number:-"))

customer=Bank(name, accno,phno)

customer.display()
customer.setnewpin(172005)
print("New Pin:-",customer.getnewpin())

customer.Deposit(5000)
customer.withdraw(3000)
customer.display()