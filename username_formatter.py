import pandas as pd

usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

cleaned = usernames.str.strip().str.lower()

print("Cleaned Usernames:")
print(cleaned)

contains_a = cleaned.str.contains('a')

print("\nContains letter 'a':")
print(contains_a)
