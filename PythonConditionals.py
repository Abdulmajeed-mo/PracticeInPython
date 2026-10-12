#conditionals
#Boolea : True or False
#condition 1
if True:
    print ("this condition 1 is True")
else:
    print ("this condition 1 is False")


#condition 2
if False:
        print ("this condition 2 is True")
else:
        print ("this condition 2 is False")



#End
print ("program Ended at first time")


#_______________________________

#comparison operators
# == : equal to
# != : not equal to
# < : less than
# > : greater than
# <= : less than or equal to
# >= : greater than or equal to

#students grade calculation

students_grade = int(input("Enter your grade: "))


if students_grade >=95:
      print("A+ grade ")
elif students_grade >=85:
            print("B+ grade ")
elif students_grade >=70:
            print("C grade ")
else:
            print("Fail grade ")

print ("program Students Grades Ended at second time")
#__________________________________________________

#Logical operators
# and : both conditions should be true  
# or : either condition should be true
# not : reverses the result, returns False if the result is true

user_name= input("Enter your username: ")
pin= int(input("Enter your pin: "))

#And operator
if user_name == "mohammed" and pin == 1234:
    print("Login successful for And operator")

else:
    print("Login failed for And operator")

#Or operator
if user_name == "mohammed" or pin == 1234:
    print("Login successful for Or operator")
else:
    print("Login failed for Or operator")

#Not operator
if not user_name == "mohammed":
    print("Login failed for Not operator")
