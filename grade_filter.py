import pandas as pd

grades = pd.Series([85, None, 92, 45, None, 78, 55])

print("Original Series:")
print(grades)

missing = grades.isnull()
print("\nMissing Values:")
print(missing)

filled = grades.fillna(0)

print("\nFilled Series:")
print(filled)

filtered = filled[filled > 60]

print("\nScores Greater Than 60:")
print(filtered)
