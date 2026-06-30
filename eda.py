# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("Titanic-Dataset.csv")

# -----------------------------
# Basic Information
# -----------------------------
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Data Cleaning
# -----------------------------
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df.drop("Cabin", axis=1, inplace=True)

# -----------------------------
# Histogram
# -----------------------------
plt.figure(figsize=(6,4))
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# Boxplot
# -----------------------------
plt.figure(figsize=(6,4))
sns.boxplot(y=df["Fare"])
plt.title("Fare Boxplot")
plt.show()

# -----------------------------
# Count Plot
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.show()

# -----------------------------
# Pair Plot
# -----------------------------
sns.pairplot(df[["Survived","Age","Fare","Pclass"]], hue="Survived")
plt.show()

# -----------------------------
# Correlation Matrix
# -----------------------------
numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# -----------------------------
# Survival by Gender
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival by Gender")
plt.show()

# -----------------------------
# Survival by Passenger Class
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="Pclass", hue="Survived", data=df)
plt.title("Survival by Passenger Class")
plt.show()

# -----------------------------
# Basic Inferences
# -----------------------------
print("\n----- INFERENCES -----")
print("1. Females had a higher survival rate than males.")
print("2. First-class passengers survived more often.")
print("3. Most passengers were between 20 and 40 years old.")
print("4. Fare contains some outliers.")
print("5. Passenger class has a negative correlation with survival.")