import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import json

# Datasets and algorithms
datasets = []
for i in range(10):
    datasets.append("Test " + str(i + 1))
algorithms = ["Quicksort", "Heapsort", "Mergesort", "Built_in_Python_Sort", "Numpy_Sort"]

# Initialize an empty list to store the data
data = []

# Loop through each algorithm and read the corresponding JSON file
for algo in algorithms:
    filename = f"{algo.lower().replace(' ', '_')}.json"
    with open(filename, 'r') as file:
        times = json.load(file)
        for i, time in enumerate(times):
            data.append({"Dataset": datasets[i], "Algorithm": algo, "Time": time})

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv("results_table.csv", index=False)

# Create a larger figure
plt.figure(figsize=(14, 8))

# Plot the data with improved aesthetics
sns.barplot(
    data=df, x="Dataset", y="Time", hue="Algorithm",
    palette="Paired", edgecolor="black"
)

# Configure titles and labels
plt.xlabel("Bộ dữ liệu", fontsize=14, fontweight='bold')
plt.ylabel("Thời gian chạy (ms)", fontsize=14, fontweight='bold')
plt.title("So sánh thời gian chạy trên các bộ dữ liệu", fontsize=16, fontweight='bold')

# Adjust the legend
plt.legend(title="Thuật toán", fontsize=12, title_fontsize=13, loc="upper right")

# Display grid for better readability
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Adjust layout to ensure everything fits
plt.tight_layout()

# Display the plot
plt.show()