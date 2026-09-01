import pandas as pd
data = {
    "ID": [1, 2, 3, 1, 4, 2],
    "Character": [
        "Barbie",
        "Ken",
        "Hermione Granger",
        "Barbie",
        "Harry Potter",
        "Ken"
    ],
    "Power_Level": [99, 85, 95, 99, 92, 85]
}
df = pd.DataFrame(data)
print("\n📊 Original DataFrame:")
print(df)
print("\n🔁 Duplicate rows check:")
print(df.duplicated())
df_no_duplicates = df.drop_duplicates()

print("\n✨ After removing duplicates:")
print(df_no_duplicates)
df_unique_characters = df.drop_duplicates(subset="Character")

print("\n🧙 Unique Characters:")
print(df_unique_characters)
df_keep_last = df.drop_duplicates(keep="last")

print("\n⏮️ Keeping last occurrence:")
print(df_keep_last)
df["Character"] = df["Character"].str.strip().str.title()

print("\n🧽 After cleaning text:")
print(df)
print("\n🧮 Number of duplicate rows:")
print(df.duplicated().sum())