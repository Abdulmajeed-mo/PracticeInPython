product_price = int(input("Enter the price of a single product : "))

quantity_products = int(input("Entering the quantity of products : "))

total = quantity_products * product_price 



if total >200 :
    discount= 0.90
    total_after_discount = discount *total
    discount_amount= total*0.10

    print (f" Total before discount :  {total}")

    print(f" Discount amount : {discount_amount} ")

    print (f" Total after discount :  {total_after_discount}")

   
else :
     
    print (f" Total before discount :  ")
    print (f" Total :  {total}")
    print (f" Total after discount :  ")


