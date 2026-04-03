import pandas as pd

DATA_PATH = "Backend/data/fashion_dataset.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset size:", len(df))
print("Columns:", df.columns)

# Check missing values
missing = df["img"].isna().sum()
print("Missing image URLs:", missing)

# Check empty strings
empty = (df["img"].str.strip() == "").sum()
print("Empty URLs:", empty)

# Check valid URLs
valid = df["img"].str.startswith("http").sum()
print("Valid URLs:", valid)

print("Dataset validation completed")