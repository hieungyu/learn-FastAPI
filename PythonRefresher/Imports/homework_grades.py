"""
-Modules get used all the time throughout
programing
- it helps with creating more files,
with unique purposes, to help with
clean maintainable code.
"""
import grade_average_service as grade_service

homework_assignment_grades = {
    "homework_1": 81,
    "homework_2": 1,
    "homework_3": 3,
    "homework_4": 100,

}

grade_service.calculate_homework(homework_assignment_grades)
