import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
darshan = pd.read_csv("../darshan_bookings(1).csv")

# ==========================
# Basic Information
# ==========================

print("First 5 Records")
print(darshan.head())

print("\nTicket Types")
print(darshan["ticket_type"].value_counts())

print("\nAverage Waiting Time:",
      round(darshan["waiting_time_min"].mean(),2),"minutes")

# ==========================
# Ticket Type Chart
# ==========================

ticket_count = darshan["ticket_type"].value_counts()

plt.figure(figsize=(8,5))

ticket_count.plot(kind="bar")

plt.title("Most Booked Darshan Ticket Types")
plt.xlabel("Ticket Type")
plt.ylabel("Bookings")

for i, value in enumerate(ticket_count):
    plt.text(i, value+0.5, str(value), ha='center')

plt.tight_layout()
plt.show()

# ==========================
# Waiting Time Histogram
# ==========================

plt.figure(figsize=(8,5))

darshan["waiting_time_min"].plot(
    kind="hist",
    bins=10
)

plt.title("Waiting Time Distribution")
plt.xlabel("Waiting Time (Minutes)")
plt.ylabel("Pilgrims")

plt.tight_layout()
plt.show()