students = ["Rahul", "Anita", "Kiran", "Priya"]

print("Students:", students)

print("First Student:", students[0])
print("Last Student:", students[-1])
students.append("Arjun")

students.remove("Kiran")


students.sort()

print("Updated List:", students)

print("\nStudent Names:")

for student in students:
    print(student)
