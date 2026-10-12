#Python Flow Control Loops
#For Loop

name = "Abdulmajeed Mohammed"

for char in name :
    print(char.upper())


# Range
for num in range(3,13) :#يطبع من 3 ويوقف قبل 13 يعني فقط يطبع ال12 ما يطبع 13
    print("i love this numbers:",num)
#مثال اخر عليها
numbers= range(4) #اذ ماحددت رقم البدايه يصير يبدا من صفر

for number in numbers:
    print (number)


# While
i =1
while i <= 5 :
    print(i)
    i +=1

#مثال اخر
i = 5
while i < 0:
    print(i)
    i -=1

