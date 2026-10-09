import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Mental Health in Tech Survey Dataset
csv_data = """Age,Gender,Country,Treatment,Work_Interfere,Remote_Work
25,Male,United States,Yes,Sometimes,No
30,Female,United States,Yes,Often,Yes
28,Male,India,No,Never,Yes
35,Female,Canada,Yes,Often,No
24,Male,India,No,Rarely,Yes
29,Female,United Kingdom,Yes,Sometimes,Yes
32,Male,United States,No,Never,No
27,Female,India,Yes,Often,Yes
40,Male,Canada,No,Rarely,No
31,Female,United States,Yes,Sometimes,Yes
26,Male,India,Yes,Rarely,No
34,Female,United Kingdom,No,Never,Yes
29,Male,United States,Yes,Often,Yes
23,Female,India,No,Sometimes,No
38,Male,Canada,Yes,Often,Yes
33,Female,United States,Yes,Sometimes,No
28,Male,India,No,Never,Yes
36,Female,United Kingdom,Yes,Rarely,Yes
42,Male,United States,No,Never,No
25,Female,India,Yes,Often,Yes
"""

# Create DataFrame
data = pd.read_csv(StringIO(csv_data))

# Display dataset
print("===== MENTAL HEALTH IN TECH SURVEY =====")
print(data)

# Dataset shape
print("\n===== DATASET SHAPE =====")
print(data.shape)

# Column names
print("\n===== COLUMN NAMES =====")
print(list(data.columns))

# Dataset information
print("\n===== DATASET INFORMATION =====")
print(data.info())

# Check missing values
print("\n===== MISSING VALUES =====")
print(data.isnull().sum())

# Statistical summary
print("\n===== STATISTICAL SUMMARY =====")
print(data.describe())

# Treatment count
print("\n===== MENTAL HEALTH TREATMENT =====")
print(data["Treatment"].value_counts())

# Gender count
print("\n===== GENDER DISTRIBUTION =====")
print(data["Gender"].value_counts())

# Country count
print("\n===== COUNTRY DISTRIBUTION =====")
print(data["Country"].value_counts())

# Remote work count
print("\n===== REMOTE WORK =====")
print(data["Remote_Work"].value_counts())

# Work interference
print("\n===== WORK INTERFERENCE =====")
print(data["Work_Interfere"].value_counts())

# Average age
print("\nAverage Age:",
      round(data["Age"].mean(), 2))

# Number of people receiving treatment
treatment_yes = (data["Treatment"] == "Yes").sum()

print("People Receiving Treatment:",
      treatment_yes)

# Percentage receiving treatment
percentage = (treatment_yes / len(data)) * 100

print("Percentage Receiving Treatment:",
      round(percentage, 2), "%")


# =========================
# VISUALIZATION
# =========================

# 1. Treatment Distribution
data["Treatment"].value_counts().plot(kind="bar")

plt.title("Mental Health Treatment Distribution")
plt.xlabel("Treatment")
plt.ylabel("Number of People")
plt.show()


# 2. Gender Distribution
data["Gender"].value_counts().plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of People")
plt.show()


# 3. Remote Work Distribution
data["Remote_Work"].value_counts().plot(kind="pie",
                                        autopct="%1.1f%%")

plt.title("Remote Work Distribution")
plt.ylabel("")
plt.show()


# 4. Age Distribution
data["Age"].plot(kind="hist", bins=8)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.show()


print("\n===== ANALYSIS COMPLETED =====")


Collab Link : ' https://colab.research.google.com/drive/1SOc5BRK8JbaHcVnTPa-IvIA1QlVDQn4Y?usp=sharing '
