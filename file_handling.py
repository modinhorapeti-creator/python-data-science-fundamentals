with open("student.txt", "w") as file:
    file.write("Student Name: Rahul\n")
    file.write("Course: Data Science\n")
    file.write("Marks: 85\n")

print("Data written successfully.")

with open("student.txt", "r") as file:
    data = file.read()

print("\nFile Contents:")
print(data)

with open("student.txt", "a") as file:
    file.write("Grade: A\n")

print("Additional data added successfully.")
