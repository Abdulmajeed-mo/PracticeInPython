#Python Data Structures: Lists & Tuples

#Lists
students =["st1" ,"std2", "st3"]

print (students[-1])# يجلب اخر عنصر
print (students[0]) #يجلب اول عنصر
print (len(students)) # تحسب عدد عناصر اللست اللي هي المصفوفه

print("-"*20)
print("Tuple")


#tuples
empty_tuple = tuple() #()

#tuple with initial values
fruits = ("Orange", "Berry", "Lemon", 653.65)
hazal_fruit = "Hazlenut", "Kiwi", "Mango", 653.65

print(fruits)
print(fruits[0])

print(type(hazal_fruit))



one_item_tuple = ("Remote Control",)
one_item_tuple2 = "Remote Control",
print(type(one_item_tuple))
print(type(one_item_tuple2))


#looping through a tuple
for fruit in fruits:
    print(fruit)


#testing if a member is in a tuple
if "Berry" in fruits:
    print("found!")

#tuple unpacking
numbers_tuple = (3, 4, 7, 10)
first_number, second_number, third_number, fourth_number = numbers_tuple


print(second_number)

#using tuple unpacking with functions
def multiply_divide(n1, n2):

    multiplication_result = n1*n2
    division_result = n1/n2

    return multiplication_result, division_result


div_result , muliply_result = multiply_divide(4, 2)

print("-"*20)


#عشان تقدر توزع العناصر على المتغيرات
# القاعدة: لازم عدد المتغيرات يساوي عدد عناصر الـ التبل.
person = ("Ali", 25, "Riyadh")
name, age, city = person

print(name,age,city)