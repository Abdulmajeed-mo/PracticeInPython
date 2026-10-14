print("=====[Calculatetor]=====")


#هنا تعاملت مع الكود  بشكل عام مو مع خطا محدد
try :
    number1 :int= int (input("Enter the first number :"))
    number2 :int= int (input ("Enter the second number :"))
    result :int =int (number1 / number2) 
    print(f"your Result is {result}")
except:
    print("only valid number")


print("----"*20)

#هنا تعاملت مع الكود والخطا بشكل مخصص 
try :
    number1 :int= int (input("Enter the first number :"))
    number2 :int= int (input ("Enter the second number :"))
    result :int =int (number1 / number2) 
    print(f"your Result is {result}")

#هنا اكسبشن محدد  ويمسك الصفر اذ بيقسمون عليه
except ZeroDivisionError :
    print("cannot divide in zero")

    #هنا يمسك الاخطاء القيمه 
except ValueError  :
    print ("pleas dont provide Chracters")

#هنا يمسك الاخطاء بشكل عام
except  Exception as error :
    print (error.__class__) #يعطيني كلاس الايرور هنا عشان اعرف بالضبط وش نوع الغلط وبعدها اقدر احط له اكسبشن محدد
    print ("something went wrong")
 

 #في حال كل المدخلات صحيحه يطبع الالس 
else :
    print("statement Successful")



finally :    #سواء نجحت العمليات او لم تنجح  في النهايه انا ابي انفذ هالعمليه
    print("statement Successful or not not matter")

    

print("----"*20)




