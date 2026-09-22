import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
donations = pd.read_csv("../donations.csv")

# ==========================
# Basic Analysis
# ==========================

print("===== First 5 Records =====")
print(donations.head())

print("\n===== Dataset Information =====")
donations.info()

print("\nTotal Donations:", len(donations))
print("Total Amount Collected: ₹", donations["amount"].sum())
print("Average Donation: ₹", round(donations["amount"].mean(), 2))
print("Highest Donation: ₹", donations["amount"].max())
print("Lowest Donation: ₹", donations["amount"].min())

# ==========================
# Payment Method Analysis
# ==========================

payment = donations["payment_method"].value_counts()

print("\nPayment Methods")
print(payment)

plt.figure(figsize=(7,5))

payment.plot(kind="bar")

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Donations")

for i, value in enumerate(payment):
    plt.text(i, value + 0.5, str(value), ha="center")

plt.tight_layout()
plt.show()

# ==========================
# Donation Amount Distribution
# ==========================

plt.figure(figsize=(8,5))

donations["amount"].plot(kind="hist", bins=10)

plt.title("Donation Amount Distribution")
plt.xlabel("Donation Amount (₹)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()