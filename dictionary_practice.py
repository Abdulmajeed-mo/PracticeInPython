# تمرين: إدارة بيانات طالب 🎯

student={
"name": "Abdulmajeed",
"age": 23,
"subjects": ["Python", "Django"]
}

print(student["name"])

student["age"]=24

student["subjects"].append("AI")

del student["age"]

for key , value in student.items():
    print(key , value)






    