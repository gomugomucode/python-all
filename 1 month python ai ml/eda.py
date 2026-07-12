# # EDA  = Exploratory Data Analysis

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. Load the data (latin-1 encoding handles the special currency symbols)
df = pd.read_csv("spam.csv", encoding="latin-1")

# 2. Drop the messy empty unnamed columns at the end
df = df.dropna(axis=1, how="all")

# 3. Rename columns to meaningful names for cleaner coding
df.columns = ["target", "text"]

# 4. Clean any unexpected leading or trailing spaces
df["target"] = df["target"].str.strip()

# 5. Encode the targets ('ham' becomes 0, 'spam' becomes 1)
encoder = LabelEncoder()
df["target"] = encoder.fit_transform(df["target"])

# 6. Generate the Pie Chart using the new target layout
plt.figure(figsize=(6, 6))
plt.pie(
    df["target"].value_counts(),
    labels=["Ham (0)", "Spam (1)"],
    autopct="%1.1f%%",
    startangle=90,
    colors=["#4CAF50", "#FF5722"],
)
plt.title("Distribution of Spam vs Ham Messages")
plt.show()









