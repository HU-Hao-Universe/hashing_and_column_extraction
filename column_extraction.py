import pandas as pd

# === Example: Sample DataFrame with sensitive and non-sensitive columns ===
data = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],                # sensitive
    "email": ["a@example.com", "b@example.com", "c@example.com"],  # sensitive
    "created_at": ["2023-01-01", "2023-01-02", "2023-01-03"],
    "Model": ["GPT-4", "GPT-3.5", "GPT-4"],
    "comments": ["Great!", "Needs improvement", "Perfect"],
    "Is_Random_Eject": [False, True, False]
}

df = pd.DataFrame(data)

# === Define columns that are safe to export (non-private) ===
non_private_columns = ["id", "created_at", "Model", "comments", "Is_Random_Eject"]

# === Save only non-private columns to CSV ===
df.to_csv("Columns_of_Interest.csv", columns=non_private_columns, index=False)

# === Optional: Preview the cleaned DataFrame ===
print(df[non_private_columns])
