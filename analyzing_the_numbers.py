number :int =int (input("Enter an integer number : "))

if number ==0 :
    print(f"this  number ({number})  is zero")

#for Even Number
elif number %2 ==0 and number > 0 :
    print(f"this number ({number}) is a positive & even number")

elif number %2 ==0 and number < 0 :
    print(f"this number ({number}) is a negative & even number")

#for Odd Number
elif number %2 !=0 and number > 0 :
    print(f"this number ({number}) is a positive & odd number")

elif number %2 !=0 and number < 0 :
    print(f"this number ({number}) is a negative & odd number")


