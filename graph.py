import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt  # Đừng quên import matplotlib để hiển thị biểu đồ
import json
# Dữ liệu giả lập: Thời gian chạy trên 3 bộ dữ liệu khác nhau
datasets = []
for i in range(10):
    datasets.append("Test " + str(i + 1))
algorithms = ["Quicksort", "Heapsort", "Mergesort", "Built_in_Python_Sort", "Numpy_Sort"]

data = []

for algo in algorithms:
    filename = f"{algo.lower().replace(' ', '_')}.json"
    with open(filename, 'r') as file:
        times = json.load(file)
        for i, time in enumerate(times):
            data.append({"Dataset": datasets[i], "Algorithm": algo, "Time": time})

df = pd.DataFrame(data)
# Create a larger figure
plt.figure(figsize=(14, 8))

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