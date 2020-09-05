# Author: Gabrielle Brunner-King gsb5225@psu.edu 

grade_1 = input("Enter your course 1 letter grade: ")
if grade_1 == "A":
  gradepoint1 = 4.0
elif grade_1 == "A-":
  gradepoint1 = 3.67
elif grade_1 == "B+":
  gradepoint1 = 3.33
elif grade_1 == "B":
   gradepint1 = 3.0
elif grade_1 == "B-":
   gradepoint1 = 2.67
elif grade_1 == "C+":
   gradepoint1 = 2.33
elif grade_1 == "C":
   gradepoint1 = 2.0
elif grade_1 == "D":
   gradepoint1 = 1.0
elif grade_1 == "F":
   gradepoint1 = 0.0
else:
   gradepoint1 = 0.0
try:
  credit_1 = float(input("Enter your course 1 credit: "))
except:
  gradepoint1 = 0.0
  credit_1 = 0.0
print(f"Grade point for course 1 is: {gradepoint1}")

grade_2 = input("Enter your course 2 letter grade: ")
if grade_2 == "A":
   gradepoint2 = 4.0
elif grade_2 == "A-":
   GP2 = 3.67
elif grade_2 == "B+":
   gradepoint2 = 3.33
elif grade_2 == "B":
   gradepoint2 = 3.0
elif grade_2 == "B-":
   gradepoint2 = 2.67
elif grade_2 == "C+":
   gradepoint2 = 2.33
elif grade_2 == "C":
   gradepoint2 = 2.0
elif grade_2 == "D":
   gradepoint2 = 1.0
elif grade_2 == "F":
   gradepoint2 = 0.0
else:
   gradepoint2 = 0.0
try:
  credit_2 = float(input("Enter your course 2 credit: "))
except:
  gradepoint2=0.0
  credit_2=0.0
print(f"Grade point for course 2 is: {gradepoint2}")

grade_3 = input("Enter your course 3 letter grade: ")
if grade_3 == "A":
   gradepoint3 = 4.0
elif grade_3 == "A-":
   gradepoint3 = 3.67
elif grade_3 == "B+":
   gradepoint3 = 3.33
elif grade_3 == "B":
   gradepoint3 = 3.0
elif grade_3 == "B-":
   gradepoint3 = 2.67
elif grade_3 == "C+":
   gradepoint3 = 2.33
elif grade_3 == "C":
   gradepoint3 = 2.0
elif grade_3 == "D":
   gradepoint3 = 1.0
elif grade_3 == "F":
   gradepoint3 = 0.0
else:
   gradepoint3 = 0.0
try:
  credit_3 = float(input("Enter your course 3 credit: "))
except:
  gradepoint3 = 0.0
  credit_3 = 0.0
print(f"Grade point for course 3 is: {gradepoint3}")

GPA = ((gradepoint1 * credit_1) + (gradepoint2 * credit_2) + (gradepoint3 * credit_3)) / (credit_1 + credit_2 + credit_3)
print(f"Your GPA is: {GPA}")