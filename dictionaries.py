student = {
    "name": "Rahul",
    "age": 21,
    "course": "Data Science",
    "marks": 85
}

print("Student Details:")

for key, value in student.items():
    print(key, ":", value)
print("\nStudent Name:", student["name"])
print("Marks:", student["marks"])

student["grade"] = "A"

print("\nUpdated Dictionary:")
print(student)
