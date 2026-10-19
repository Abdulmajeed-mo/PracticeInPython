# Student Management System

#class
class Student :
    #Attribute
    def __init__ (self , name , age) :
        self.name = name
        self.age = age
    #Method
    def display_info(self ) :
       print (f"Student Name : {self.name} \n Student Age : {self.age}")


#Object 

student1=student ("Abdulmajeed", "24")

student2 = student("Mansoor","23")


#call the method
student1.display_info()

student2.display_info()


       
