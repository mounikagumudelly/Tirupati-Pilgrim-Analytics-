import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Read Dataset
# ==========================


pilgrims = pd.read_csv("../pilgrims.csv")
darshan = pd.read_csv("../darshan_bookings(1).csv")
prasadam = pd.read_csv("../prasadam_orders.csv")
donations = pd.read_csv("../donations.csv")
transport = pd.read_csv("../transport.csv")
accommodation = pd.read_csv("../accommodation.csv")
print(darshan.columns)
# ==========================
# Data Cleaning
# ==========================

# Remove extra spaces
pilgrims["gender"] = pilgrims["gender"].str.strip()

# Convert to lowercase
pilgrims["gender"] = pilgrims["gender"].str.lower()

# Fix spelling mistakes and standardize values
pilgrims["gender"] = pilgrims["gender"].replace({
    "male": "Male",
    "female": "Female",
    "femlae": "Female",
    "femail": "Female"
})

# Clean state names
pilgrims["state"] = pilgrims["state"].str.strip().str.title()

# ==========================
# Basic Analysis
# ==========================

print("\n===== First 5 Records =====")
print(pilgrims.head())

print("\n===== Dataset Info =====")
pilgrims.info()

print("\nTotal Pilgrims:", len(pilgrims))

print("\n===== Gender Distribution =====")
print(pilgrims["gender"].value_counts())

print("\n===== State-wise Pilgrims =====")
print(pilgrims["state"].value_counts())

print("\nAverage Age:", round(pilgrims["age"].mean(), 2))
print("Oldest Age:", pilgrims["age"].max())
print("Youngest Age:", pilgrims["age"].min())

# ==========================
# State-wise Bar Chart
# ==========================

plt.figure(figsize=(8,5))

state_count = pilgrims["state"].value_counts()

state_count.plot(kind="bar")

plt.title("State-wise Pilgrim Distribution", fontsize=16)
plt.xlabel("State")
plt.ylabel("Number of Pilgrims")
plt.xticks(rotation=45)

# Display values on bars
for i, value in enumerate(state_count):
    plt.text(i, value + 0.5, str(value), ha='center')

plt.tight_layout()
plt.show()

# ==========================
# Gender Pie Chart
# ==========================

gender_data = pilgrims["gender"].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    gender_data.values,
    labels=gender_data.index,
    autopct="%1.1f%%",
    startangle=90,
    explode=(0.05, 0.05),
    shadow=True
)

plt.title("Gender Distribution of Pilgrims", fontsize=16)
plt.axis("equal")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
pilgrims = pd.read_csv("../pilgrims.csv")

# Clean gender column
pilgrims["gender"] = pilgrims["gender"].str.strip().str.lower()

pilgrims["gender"] = pilgrims["gender"].replace({
    "male": "Male",
    "female": "Female",
    "femlae": "Female",
    "femail": "Female"
})

gender_data = pilgrims["gender"].value_counts()

plt.figure(figsize=(7,7))

plt.pie(
    gender_data.values,
    labels=gender_data.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gender Distribution of Pilgrims")
plt.axis("equal")

plt.show()
# ==========================
# Darshan Ticket Analysis
# ==========================

print("\n===== Ticket Type Distribution =====")
print(darshan["ticket_type"].value_counts())

ticket_count = darshan["ticket_type"].value_counts()

plt.figure(figsize=(7,5))

ticket_count.plot(kind="bar")

plt.title("Most Booked Darshan Ticket Types")
plt.xlabel("Ticket Type")
plt.ylabel("Number of Bookings")

for i, value in enumerate(ticket_count):
    plt.text(i, value + 0.5, str(value), ha="center")

plt.tight_layout()
plt.show()
# ==========================
# Waiting Time Analysis
# ==========================

print("\nAverage Waiting Time:",
      round(darshan["waiting_time_min"].mean(),2), "minutes")

plt.figure(figsize=(8,5))

darshan["waiting_time_min"].plot(
    kind="hist",
    bins=10
)

plt.title("Waiting Time Distribution")
plt.xlabel("Waiting Time (Minutes)")
plt.ylabel("Number of Pilgrims")

plt.tight_layout()
plt.show()