def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

marks = int(input("Enter marks: "))
grade = get_grade(marks)

print("Grade =", grade)