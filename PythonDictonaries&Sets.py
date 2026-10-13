# Python Data Structures:Dictionaries & Sets

# Dictionaries
students ={
    "name":"abdulmajeed" ,
    "age" : 23
}

print(students["name"])

#delete the key
del students["age"]
print(students)

print("--"*20)

# for in Dictionaries

color_fruits={
    "apple": ["red" ,"green"],
   "carrot" : "orange",
   "banana": "yellow"
 }

print(color_fruits["apple"][0])

#اضافه لون اصفر في اللست
color_fruits["apple"].append("yellow")

#يطبع لك الكي فقط
for key in color_fruits:
     print(key)

#يطبع الفاليو فقط
for value in color_fruits.values():
    print(value)
print("--"*20)


#تمر على الفاليو والكي
for key , value in color_fruits.items():
    print(key , value)

print("--"*20)

# Sets
fruits = {"apple", "banana", "apple", "orange"}
#لا يسمح بتكرار العناصر
print(fruits)



print("--"*20)


languages = {"Python", "JavaScript"}

languages.add("Django")       # إضافة عنصر
languages.remove("Python")   # حذف عنصر موجود
languages.discard("Java")    # حذف دون خطأ إذا لم يكن موجودًا

print("--"*20)

# for Loop in Sets 
languages = {"Python", "Java", "C#"}

for language in languages:
    print(language)


print("--"*20)
print("--"*20)
my_set = {1, 2, 3}      # إنشاء Set
my_set.add(4)           # إضافة عنصر
my_set.remove(2)        # حذف عنصر موجود
my_set.discard(5)       # حذف دون خطأ إذا لم يوجد

for item in my_set:     # المرور على العناصر
    print(item)