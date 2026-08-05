import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = "uploads/student_placement_prediction_dataset_2026.csv"
df=pd.read_csv(file_path)

plt.figure(figsize=(8,5))
plt.hist(df["age"],bins=10,edgecolor="black")
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis="y",linestyle="--",alpha=0.5)
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["cgpa"], bins=10, edgecolor="black")
plt.title("CGPA Distribution")
plt.xlabel("CGPA")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.grid(axis="y",linestyle="--",alpha=0.5)
plt.show()

plt.figure(figsize=(6,4))
plt.boxplot(df["age"])
plt.title("Box Plot of Age")
plt.ylabel("Age")
plt.show()

plt.figure(figsize=(6,4))
df["branch"].value_counts().plot(kind="bar")
plt.title("Students by Branch")
plt.xlabel("Branch")
plt.ylabel("Number of Students")
plt.show()