import pandas as pd

data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Python": [85, 72, 90, 65, 88],
    "Statistics": [80, 75, 92, 60, 85],
    "Data_Science": [88, 70, 95, 68, 90]
}

df = pd.DataFrame(data)

df["Average"] = (
    df["Python"] +
    df["Statistics"] +
    df["Data_Science"]
) / 3

print("Student Performance:")
print(df)

top_student = df.loc[df["Average"].idxmax()]

print("\nTop Performing Student:")
print(top_student)

class_average = df["Average"].mean()

print("\nClass Average:", round(class_average, 2))
print("\nStudents Above Class Average:")
print(df[df["Average"] > class_average])
