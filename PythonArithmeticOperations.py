#Python Arithmetic Operations
#addition عملية الجمع
print(13+3)

#subtraction عملية الطرح
print(13-3)

#multiplication عملية الضرب
print(13*3)

#division عملية القسمة
print(13/3)
print(type(13/3)) #نوع البيانات الناتج من القسمة 

#floor division
#عملية القسمه مع التقريب لاقرب عدد صحيح  من ناحية الاقل
#دايم يكون الناتج انتيجر"int"
print(13//3) #floor division القسمة الصحيحة

#modulus operation
print(13%3) #modulus باقي القسمة

#exponentiation operation عملية الأس
print(5**2) #exponentiation raising to a power

#precedence of operations
#ترتيب العمليات الحسابية    
print(2+3*4)
#Note:
#PEMDAS
#-parentheses
#-exponentiation
#-multiplication and division
#-addition and subtraction

#left biding operations
#عمليات الربط من اليسار لليمين
print(5+6/3 *2) 

#ترتيب العمليات
print((5+6)/3 *2) #تجمع اولا  
print(5**2+2)
print(5**(2*2))


#ُExponentiation are right Binding operations
print(2**3**5) #2**(3**5)

#التقريب
#rounding to the nearest integer
#تستخدم دالة راوند لتقريب الرقم الى اقرب عدد صحيح
result = round(5+6)/3*2    
print(round(result))

#اذ تبي يقرب لك لرقم تبيه خاص بالفواصل يع يعني يخلي الفاوصل العشريه  مو عدد دوري بل عدد انت تتحدده
#rounding to a specific number of decimal places
result = round(5+6)/3*2
print(round(result, 3)) #rounding to 3 decimal places

