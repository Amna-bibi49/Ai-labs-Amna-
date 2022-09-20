# python program for grading system

marks = float(input("Enter your marks i: "))

if marks >= 91:
    print("Grade: A")
elif marks >= 81 and marks <= 90:
    print("Grade:B ")
elif marks >= 71 and marks <= 80:
    print("Grade: C")
elif marks >= 61 and marks <= 70:
    print("Grade: D")
elif marks >= 50 and marks <= 60:
    print("Grade: E")
else:
    print("Grade: F")
