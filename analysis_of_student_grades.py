student_grades=[]



for grade in range(5) :
    user_input = int(input("Please enter the grade here : "))
    
    student_grades.append(int(user_input))
    

successful_count=0

for successful in student_grades :
    if successful >=60 :
        successful_count +=1

print("Congratulations to these students who have succeeded:",successful_count)



total = sum(student_grades)
maximum = max(student_grades)
average = total / len(student_grades)

print("the total:", total)
print(" the max number : ", maximum)
print(" the average : ", average)
