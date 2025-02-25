#Experiment No : 9
#Name of the Experiment : Create a Python application for a simple Student 
#Management System. The application should include the following functionalities:
#Class Definition: Define a Student class that:
#Has instance variables name and age.
#Has a class variable college_name that is shared among all instances.
#Methods: Implement the following methods within the Student class:
class Student:
    college_name="Presidency University"
    
    def __init__(self,name,age):
       self.name=name
       self.age=age
    #Instance Methods:
    #get_details(): Returns the details of the student (name, age, and college name).   
    def getdetails(self):
        return f"Name:-{self.name} age:-{self.age} college name:-{self.college_name} "
    #change_college(new_college): Allows changing the college_name for all instances 
    #of Student.
    @classmethod
    def change_collage(cls,new_college):
        cls.college_name=new_college
        
     #Static method to check if the student is an adult
     #Static Methods:
     #is_adult(age): Takes an age as input and returns True if the age is 18 or above, otherwise 
     #returns False.
    def isAdult(age):
        if age >=10:
            return True
        else:
            return False
        
        '''  Inner Class: Create an inner class called Address that has attributes city and state.
        It should 
also have a method get_address() to return the address details.
Data Transfer Between Classes: Define another class called Course. This class should:
Accept a Student object during initialization and store its details.
Have a method get_student_info() that returns the details of the student in that course.
'''
    class Address:
        def __init__(self,city,state):
            self.city=city
            self.state=state
            
        def get_address(self):
            return f"city:-{self.city} state:-{self.state}"
        
#Another class to associate a student with a course
class Course:
    def __init__(self,Studet):
         self.Student=Student
         
    # Method to get student info in the course
    def get_student_info(self):
        return self.Student.getdetails()
    
    
Student1=Student("Rahula",20)
Student2=Student("Anni",10)

print(Student1.getdetails())
print(Student2.getdetails())

# Checking if the students are adults
print(Student.isAdult(Student1.age))
print(Student.isAdult(Student2.age))


#Changing the college for all students
Student.change_collage("IIT")
print(Student1.getdetails())
print(Student2.getdetails())

#Get The Student Address
print(Student1.Address("Bengaluru", "karnataka").get_address())
print(Student2.Address("Mysore","karnataka").get_address())

# Creating Course object with student1
course1=Course(Student1)
course2=Course(Student2)
print("Student Info In the Corse:-",course1.get_student_info())
