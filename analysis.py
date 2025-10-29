import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
from pathlib import Path

df = pd.read_csv("spam.csv", encoding="latin-1")
df = df.rename(columns={"Category": "label", "Message": "message"})
df = df[["label", "message"]].dropna()

def clean_text(s):
    s = s.lower()
    return s.translate(str.maketrans("", "", string.punctuation))

df["clean_text"] = df["message"].apply(clean_text)
df["char_count"] = df["clean_text"].str.len()
df["word_count"] = df["clean_text"].str.split().str.len()

print("\n=== BASIC DATA OVERVIEW ===")
print(df.head())
print("\nDataset shape:", df.shape)
print("\nLabel distribution:\n", df["label"].value_counts())
print("\nAverage word count per label:\n", df.groupby("label")["word_count"].mean())

sns.set(style="whitegrid")
out = Path("figs"); out.mkdir(exist_ok=True)
plt.rcParams["figure.dpi"] = 150

plt.figure(figsize=(5,3))
sns.countplot(x="label", data=df)
plt.title("Message Category Distribution")
plt.xlabel("Category"); plt.ylabel("Count")
plt.tight_layout(); plt.savefig(out / "category_counts.png"); plt.close()

plt.figure(figsize=(6,4))
sns.histplot(data=df, x="word_count", hue="label", bins=30, kde=True)
plt.title("Word Count Distribution by Category")
plt.xlabel("Word Count"); plt.ylabel("Frequency")
plt.tight_layout(); plt.savefig(out / "wordcount_hist.png"); plt.close()

plt.figure(figsize=(6,4))
sns.boxplot(x="label", y="char_count", data=df)
plt.title("Character Count by Category")
plt.xlabel("Category"); plt.ylabel("Character Count")
plt.tight_layout(); plt.savefig(out / "charcount_box.png"); plt.close()

print("\n=== INSIGHTS ===")
print(f"Total messages: {len(df)}")
spam_ratio = df['label'].value_counts(normalize=True).get('spam', 0.0)
print(f"Spam ratio: {spam_ratio:.2%}")
print("Spam messages are typically longer; ham messages are shorter/conversational.")

print("\nSaved plots:")
for p in sorted(out.glob("*.png")):
    print(" -", p)