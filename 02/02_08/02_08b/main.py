my_list = [1, 7, 3]
print(sorted(my_list, reverse=True))

student_grades = [("Stu_A", 38), ("Stu_B", 47), ("Stu_C", 84)]
print(sorted(student_grades))
print(sorted(student_grades, key=lambda x:x[1], reverse=True))