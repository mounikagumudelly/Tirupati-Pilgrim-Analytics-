import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Read Dataset
# ==========================

accommodation = pd.read_csv("../accommodation.csv")

# ==========================
# Basic Analysis
# ==========================

print("===== First 5 Records =====")
print(accommodation.head())

print("\n===== Dataset Information =====")
accommodation.info()

print("\nTotal Bookings:", len(accommodation))
print("Total Revenue: ₹", accommodation["room_charge"].sum())
print("Average Room Charge: ₹", round(accommodation["room_charge"].mean(), 2))
print("Highest Room Charge: ₹", accommodation["room_charge"].max())
print("Lowest Room Charge: ₹", accommodation["room_charge"].min())

# ==========================
# Room Type Analysis
# ==========================

room_count = accommodation["room_type"].value_counts()

print("\nRoom Type Distribution")
print(room_count)

plt.figure(figsize=(8,5))

room_count.plot(kind="bar")

plt.title("Room Type Distribution")
plt.xlabel("Room Type")
plt.ylabel("Number of Bookings")

for i, value in enumerate(room_count):
    plt.text(i, value + 0.5, str(value), ha="center")

plt.tight_layout()
plt.show()

# ==========================
# Room Charge Distribution
# ==========================

plt.figure(figsize=(8,5))

accommodation["room_charge"].plot(kind="hist", bins=10)

plt.title("Room Charge Distribution")
plt.xlabel("Room Charge (₹)")
plt.ylabel("Number of Bookings")

plt.tight_layout()
plt.show()