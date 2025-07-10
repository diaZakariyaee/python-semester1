#               0    1    2    3    4
students = {"Arsham,Diana,Dia,Dilan,Kian"}

students.sort()
students.reverse()

print(students[3])
students.append("Nooran beheshti")
print(f"list of students :\n {students}")

students.remove("Nooran beheshti")

print(f"list of students :\n {students}")

students.insert(2,"Kian")
print(f"list of students :\n {students}")

print(f"list of students :\n {students}")