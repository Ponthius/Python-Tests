students = ["Poel", "Brait", "Paul", "Ponthius"]
print(len(students))
students[2] = "Dedan"
students.append("Josh")
students.insert(1, "Sarah")
students.remove("Dedan")
last_student = students.pop()
print(last_student)
#students.sort()
print(students)
students.reverse()
print("Brait" in students)
num = students.count("Ponthius")
print(num)
for student in students:
    print(student)