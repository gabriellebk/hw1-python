#Author: Gabrielle Brunner-King gsb5225@psu.edu 

grade_1 = str(input("Enter your course 1 letter grade: "))
credit_1 = float(input("Enter your course 1 credit: "))

if grade_1 == "A":
  gradepoint_1 = 4.0
elif grade_1 == "A-":
  gradepoint_1 = 3.67
elif grade_1 == "B+":
  gradepoint_1 = 3.33
elif grade_1 == "B":
  gradepoint_1 = 3.0
elif grade_1 == "B-":
  gradepoint_1 = 2.67
elif grade_1 == "C+":
  gradepoint_1 = 2.33
elif grade_1 == "C":
  gradepoint_1 = 2.0
elif grade_1 == "D":
  gradepoint_1 = 1.0
else: 
  gradepoint_1 = 0
print(f"Grade point for course 1 is: {float(gradepoint_1)}")
grade_2 = str(input("Enter your course 2 letter grade: "))
credit_2 = float(input("Enter your course 2 credit: "))

if grade_2 == "A":
  gradepoint_2 = 4.0
elif grade_2 == "A-":
  gradepoint_2 = 3.67
elif grade_2 == "B+":
  gradepoint_2 = 3.33
elif grade_2 == "B":
  gradepoint_2 = 3.0
elif grade_2 == "B-":
  gradepoint_2 = 2.67
elif grade_2 == "C+":
  gradepoint_2 = 2.33
elif grade_2 == "C":
  gradepoint_2 = 2.0
elif grade_2 == "D":
  gradepoint_2 = 1.0
else:
  gradepoint_2 = 0
print(f"Grade point for course 2 is: {float(gradepoint_2)}")
grade_3 = str(input("Enter your course 3 letter grade: "))
credit_3 = float(input("Enter your course 3 credit: "))

if grade_3 == "A":
  gradepoint_3 = 4.0
elif grade_3 == "A-":
  gradepoint_3 = 3.67
elif grade_3 == "B+":
  gradepoint_3 = 3.33
elif grade_3 == "B":
  gradepoint_3 = 3.0
elif grade_3 == "B-":
  gradepoint_3 = 2.67
elif grade_3 == "C+":
  gradepoint_3 = 2.33
elif grade_3 == "C":
  gradepoint_3 = 2.0
elif grade_3 == "D":
  gradepoint_3 = 1.0
else:
  gradepoint_3 = 0
print(f"Grade point for course 3 is: {float(gradepoint_3)}")

GPA = (gradepoint_1 * credit_1 + gradepoint_2 * credit_2 + gradepoint_3 * credit_3) / (credit_1 + credit_2 + credit_3) 
print(f"Your GPA is: {GPA}")
