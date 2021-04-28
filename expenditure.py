#navgurukul ke ek bache ka kharcha


number_student=int(input("how many student are in ng?"))
print("total expenditure of student in navgurukul of one month")
expenditure_student=int(input("expenditure of student"))
total=number_student*expenditure_student
print("total amount of expenditure",total)
if total<=50000:
    print("hum budget ke andar hain")
else:
    print("hum budget ke bahar hain")
