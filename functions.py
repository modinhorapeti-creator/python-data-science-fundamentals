def greet(name):
    return "Hello, " + name + "!"

def add_numbers(a, b):
    return a + b

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


print(greet("Student"))

result = add_numbers(10, 20)
print("Sum:", result)

marks = [80, 75, 90, 85, 70]
average = calculate_average(marks)

print("Marks:", marks)
print("Average:", average)
