NAME = input("enter name:-")
English = int(input("enter marks:-"))
Statics = int(input("enter marks:-"))
Account = int(input("enter marks:-"))
Economic = int(input("enter marks:-"))
OC = int(input("enter marks:-"))
Hindi = int(input("enter marks:-"))


total = English+Statics+Account+Economic+OC+Hindi
print(total)

out_of = 600
percentage = (total / out_of) * 100
print(round(percentage, 2))
if percentage >= 90:
	print("A+")
elif percentage >= 80:
	print("A2")
elif percentage >= 70:
	print("B1")
elif percentage >= 60:
	print("B2")
elif percentage >= 50:
	print("D1")
elif percentage >= 40:
	print("D2")
elif percentage >= 34:
	print("E")
elif percentage >= 33:
	print("PASS")
else:
	print("FAIL")
	
	
#marksheet ui/
print(f"{'Marksheet': ^35}")

print("-"*35)

print(f"{'Subject': <15}{'Total': <10}{'Marks'}")
print("-"*35)
 
print(f"{'English': <15}{'100': <10}{English}")

 
print(f"{'Statics': <15}{'100': <10}{Statics}")

 
print(f"{'Account': <15}{'100': <10}{Account}")


 
print(f"{'Economic': <15}{'100': <10}{Economic}")


 
print(f"{'OC': <15}{'100': <10}{OC}")


 
print(f"{'Hindi': <15}{'100': <10}{Hindi}")



print("-"*35)
print(f"{'  ': <15}{'600': <10}{total}")

print("-"*35)

print("Student Name :-",NAME.capitalize())
print("Percentage:-",round(percentage,2))

if percentage >= 90:
	print("Grade:- A+")
elif percentage >= 80:
	print("Grade:- A2")
elif percentage >= 70:
	print("Grade:- B1")
elif percentage >= 60:
	print("Grade:- B2")
elif percentage >= 50:
	print("Grade:- D1")
elif percentage >= 40:
	print("Grade:- D2")
elif percentage >= 34:
	print("Grade:- E")
elif percentage >= 33:
	print("Grade:- PASS")
else:
	print("Grade:- FAIL")

if percentage >= 34:
	print("Result:- PASS")
else:
	Print("Result:- Fail")
	