import re
import matplotlib.pyplot as plt

# ======= Step 1: Read and extract TOF values =======
tof_values = []
with open("Time_of_Flight_1.txt", "r") as file:
    for line in file:
        match = re.search(r'TOF\(([\d.]+) usec\)', line)
        if match:
            tof = float(match.group(1))
            tof_values.append(tof)

# ======= Step 2: Plot histogram =======
plt.figure(figsize=(8, 5))
plt.hist(tof_values, bins=100, color='skyblue', edgecolor='black')
plt.xlabel("Time of Flight (µs)")
plt.ylabel("Ion Count")
plt.title("Histogram of Time of Flight (TOF)")
plt.grid(True)

# ======= Step 3: Save or show plot =======
plt.tight_layout()
plt.savefig("tof_histogram.png", dpi=300)
plt.show()
