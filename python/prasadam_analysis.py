import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Read Dataset
# ==========================

prasadam = pd.read_csv("../prasadam_orders.csv")

# ==========================
# Basic Analysis
# ==========================

print("===== First 5 Records =====")
print(prasadam.head())

print("\n===== Dataset Information =====")
prasadam.info()

print("\nTotal Orders:", len(prasadam))

print("Total Revenue: ₹", prasadam["amount"].sum())

print("Average Order Amount: ₹", round(prasadam["amount"].mean(),2))

print("Most Ordered Prasadam")
print(prasadam["prasadam_type"].value_counts())

# ==========================
# Prasadam Type Chart
# ==========================

prasadam_count = prasadam["prasadam_type"].value_counts()

plt.figure(figsize=(8,5))

prasadam_count.plot(kind="bar")

plt.title("Most Ordered Prasadam")
plt.xlabel("Prasadam Type")
plt.ylabel("Number of Orders")

for i, value in enumerate(prasadam_count):
    plt.text(i, value + 0.5, str(value), ha='center')

plt.tight_layout()
plt.show()

# ==========================
# Quantity Distribution
# ==========================

plt.figure(figsize=(8,5))

prasadam["quantity"].plot(kind="hist", bins=10)

plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.show()