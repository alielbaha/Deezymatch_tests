import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter

# Example list of counts
data = [5, 8, 12, 15, 7, 10, 10, 14, 18, 6, 9, 13, 11, 17, 16, 5, 8, 7, 12, 14]

# Histogram - Shows frequency distribution
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(data, bins=7, kde=True, color='blue')
plt.xlabel("Count of Elements")
plt.ylabel("Frequency")
plt.title("Histogram of Element Counts")

# Bar Chart - Shows unique counts and their frequency
plt.subplot(1, 2, 2)
count_dict = Counter(data)  # Count occurrences of each number
plt.bar(count_dict.keys(), count_dict.values(), color='orange')
plt.xlabel("Element Count")
plt.ylabel("Frequency")
plt.title("Bar Chart of Element Frequencies")

plt.tight_layout()
plt.show()

# Box Plot - Shows spread and outliers
plt.figure(figsize=(6, 4))
sns.boxplot(x=data, color="green")
plt.title("Box Plot of Element Counts")
plt.show()
