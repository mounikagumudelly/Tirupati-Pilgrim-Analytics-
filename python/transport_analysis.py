import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Read Dataset
# ==========================

transport = pd.read_csv("../transport.csv")

# ==========================
# Basic Analysis
# ==========================

print("===== First 5 Records =====")
print(transport.head())

print("\n===== Dataset Information =====")
transport.info()

print("\nTotal Transport Bookings:", len(transport))

print("\nTransport Mode Distribution")
print(transport["transport_mode"].value_counts())

# ==========================
# Transport Mode Bar Chart
# ==========================

transport_count = transport["transport_mode"].value_counts()

plt.figure(figsize=(8,5))

transport_count.plot(kind="bar")

plt.title("Transport Mode Used by Pilgrims")
plt.xlabel("Transport Mode")
plt.ylabel("Number of Pilgrims")

for i, value in enumerate(transport_count):
    plt.text(i, value + 0.5, str(value), ha="center")

plt.tight_layout()
plt.show()

# ==========================
# Transport Mode Pie Chart
# ==========================

plt.figure(figsize=(7,7))

plt.pie(
    transport_count.values,
    labels=transport_count.index,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Transport Mode Distribution")
plt.axis("equal")

plt.show()