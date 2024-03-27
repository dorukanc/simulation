import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd


df = pd.read_excel('../data/w6L2.xlsx')
df.head()

# Histogram of the dataset

bin_sizes = [5, 10, 20, 25, 50]

# Create subplots
fig, axs = plt.subplots(1, 5, figsize=(16,5))


for i, bins in enumerate(bin_sizes):
    axs[i].hist(df['data1'], bins=bins, color='red', edgecolor='black')
    axs[i].set_title(f'Bin size = {bins}')
    axs[i].set_xlabel('Data 1')
    axs[i].set_ylabel('Frequency')

# Adjust layout
plt.tight_layout()

# Display histograms

plt.show()



