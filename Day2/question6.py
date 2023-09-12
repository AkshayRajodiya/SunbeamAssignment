# The marks obtained by a student in 3 different subjects are input by the user. Your program should
# calculate the average of subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F.
def calculate_grades(sub1, sub2, sub3):
    if sub1 > 100 or sub2 > 100 or sub3 > 100:
        print("subject marks should be not greater than 100")
        return
    average = (sub1 + sub2 + sub3) // 3
    if average >= 90:
        print(f"Grade : A and Average = {average}")
    elif 90 > average >= 80:
        print(f"Grade : B and Average = {average}")
    elif 80 > average >= 70:
        print(f"Grade : C and Average = {average}")
    elif 70 > average >= 60:
        print(f"Grade : D and Average = {average}")
    else:
        print(f"Grade : F and Average = {average}")


calculate_grades(101, 105, 90)
calculate_grades(100, 95, 90)
calculate_grades(90, 80, 90)
calculate_grades(70, 80, 60)
calculate_grades(60, 65, 70)
calculate_grades(50, 57, 56)
