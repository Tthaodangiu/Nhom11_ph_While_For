#Tính trung bình các số nhập vào
print("Enter the letter grades (press Enter after each grade, and leave blank to finish):")
grade_points = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7,
                    "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}

total_grade_points = 0
num_grades = 0
grade = input()
while grade != "":
    for digit in grade_points:
        total_grade_points += grade_points[grade]
        num_grades += 1

    if num_grades > 0:
        gpa = total_grade_points / num_grades
    else:
        gpa = 0.0
    grade = input()
print("The point average is:", round(gpa,1))