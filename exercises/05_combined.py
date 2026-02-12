"""
TODO:
Dictionary of students -> grades
Print averages
"""

students_grades = {
    "Rena": [88, 92, 79],
    "Shifra": [75, 85, 91],
    "Chaim": [90, 87, 93],
    "Sari": [100, 95, 98]
}

for student, grades in students_grades.items():
    avg = sum(grades) / len(grades)
    print(f"{student}'s average: {avg:.2f}")