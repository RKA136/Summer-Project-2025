import re
import matplotlib.pyplot as plt
def plot_histogram(filename, bins):
    # ======= Step 1: Read file and extract TOF values =======
    tof_values = []
    with open(f"TOF_ritam/data/{filename}.txt", "r") as file:
        for line in file:
            # Look only for lines with TOF values
            match = re.search(r'TOF\(([\d.]+) usec\)', line)
            if match:
                tof = float(match.group(1))  # in microseconds
                tof_values.append(tof)

    # ======= Step 2: Plot histogram =======
    plt.figure(figsize=(8, 5))
    plt.hist(tof_values, bins=bins, color='steelblue', edgecolor='black')
    plt.xlabel("Time of Flight (µs)")
    plt.ylabel("Ion Count")
    plt.title("Histogram of Ion TOF")
    plt.grid(True)

    # ======= Step 3: Save or show =======
    plt.tight_layout()
    plt.savefig(f"TOF_ritam/figures/{filename}.png", dpi=300)
    plt.close()

