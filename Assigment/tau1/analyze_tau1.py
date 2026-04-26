import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load datas
df = pd.read_csv("times.csv")
times = df["time_ns"].values 

# Define statistics 
minimum = np.min(times)
q1 = np.percentile(times, 25)
q2 = np.percentile(times, 50)
q3 = np.percentile(times, 75)
before_max = np.percentile(times, 99.9)
maximum = np.max(times)
mean = np.mean(times)
std_deviation = np.std(times)

# Convert the worst case :
C1_us = maximum / 1e3
C1_ms = maximum / 1e6

# Results : 
print("Execution time statistics for tau1 : \n")
print(f"Number of samples : {len(times)} \n")
print(f"Min: {minimum} ns \n")
print(f"Q1 : {q1} ns \n")
print(f"Q2 : {q2} ns \n")
print(f"Q3 : {q3} ns \n")
print(f"Before max : {before_max} ns \n")
print(f"Max: {maximum} ns \n")
print(f"Mean : {mean} ns \n")
print(f"Std : {std_deviation} ns \n")
print(f"WCET C1 = {maximum} ns / {C1_us} us / {C1_ms} ms \n")

# Distribution Analysis
fig, ax = plt.subplots(figsize=(8, 4))
fig.suptitle("Execution time analysis — tau1", fontsize = 13, fontweight = "bold")

ax.hist(times, bins = 60, color = "#4C72B0", edgecolor = "white", linewidth = 0.4)
ax.axvline(maximum, color = "red",    linestyle = "--", linewidth = 1, label=f"WCET = {maximum} ns")
ax.axvline(minimum, color = "green",  linestyle="--", linewidth=1, label=f"Min = {minimum} ns")
ax.axvline(q2, color = "orange", linestyle = "--", linewidth = 1, label = f"Median = {q2} ns")
ax.axvline(before_max, color = "magenta", linestyle = "--", linewidth = 1, label = f"Before max (99.9) = {before_max} ns")
ax.set_title("Time distribution")
ax.set_xlabel("Time (ns)")
ax.set_ylabel("Frequency")
ax.legend()

plt.tight_layout()
plt.savefig("tau1_analysis_100000.png", dpi=150)
plt.show()
