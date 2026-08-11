import pandas as pd

data = {
    "Name": ["Rahul", "Anita", "Kiran", "Priya", "Arjun"],
    "Age": [21, 22, 20, 21, 23],
    "Marks": [85, 90, 75, 88, 95]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nStudents with Marks above 80:")
print(df[df["Marks"] > 80])
