#Python functions

def greet_user():
    print ("welcome in our Programm ")


#calling the Function
greet_user ()



#define function with parametrs

                   #ذي تسمى parameters
def multiplication (x:int , y :int) :
    total=x*y    #هنا عرفنا متغير وسوينا فيه عمليات حسابيه 
    
          #String Format
    print(f"this your total : {total}") #هنا استسخدمنا الفورمات عشان ندخل القيمه من ضمن النص

#وقت الاسدعاء تسمى ما بداخل الاقواس argument
#passing the argument to the function
multiplication(4,5) # هنا استدعائها 




#function with return

def calculate_bmi ( weight:int ,height:float ):
    '''this function its for Calculate The BMI '''
    bmi=weight/height**2
    return round(bmi,2)

            #بمعنى اني سويت للداله استدعاء
             #وهنا حطينا ناتج الداله في متغير
bmi_result =calculate_bmi(70 ,1.68 ) 
print(bmi_result)

print("_"*23)


#Functions 102

username:str = input("username: ")
password:str = input("password: ")

def login_user():
    global username
    system_version = 5.2
    username = "ahmed"
    print(username)
    if username == "majeed" and password == "1235":
        print(f"welcome to our system")
        print(f"version {system_version}")
    else:
        print("You are not authorized")


login_user()
print(username)


#Positional arguments: Args, keyword arguments: Kwargs

def rectangle_area(height:float, width:float, unit:str = "meter") -> float:
    """
    this calculates the area of a rectangle in the unit provided

    Args:
    """