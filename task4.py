import pandas as pd

# Creating a Series for student marks
marks = pd.Series([85, 92, 78], index=['Riaz', 'Afreen', 'Saddam'])

print("--- Student Marks Series ---")
print(marks)

# Accessing data by the label (Label-based indexing)
print(f"\nMarks for Riaz: {marks['Riaz']}")

# Performing math (Vectorization works here too!)
print("\nMarks after 5 bonus points:")
print(marks + 5)