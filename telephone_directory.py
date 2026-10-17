telephone_directory = {

"Amal":	"1111111111" ,
"Mohammed":	"2222222222",
"Khadijah":	"3333333333",
"Abdullah" :	"4444444444",
"Rawan" :	"5555555555",
"Faisal" :	"6666666666",
"Layla"   :"7777777777"
}


number: str =input("Enter Phone Number :")



#check the number 
def check_number (): 
    if len(number) == 10  and number.isdigit() :
         return True 
    else :
        return False

#search by number funciton
def search_by_number ():
    for key , value in telephone_directory.items():
        if value ==number:
             print( key)
             break
        
    else :
          print ("Sorry, the number is not found ")
    return









def main ():
    if check_number () ==True :
         search_by_number()
    else :
        print("This is invalid number")



main()

print("---"*13)


user_name: str = input("Enter The Name :")
#search by name
def search_by_name ():
    for key , value in telephone_directory.items():
        if key == user_name:            
            print(f" the name :{key} \n the number : {value}")
            break
    else :
        print("Name not found")


search_by_name()