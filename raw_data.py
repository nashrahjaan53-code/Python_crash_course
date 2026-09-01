import pandas as pd

print("🔥 File is running 🔥")

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