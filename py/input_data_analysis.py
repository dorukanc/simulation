import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon, norm
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


# Fit data to a normal distribution
mu_normal, std_normal = norm.fit(df['data1'])

# Fit data to an exponential distribution
loc_exponential, scale_exponential = expon.fit(df['data1'])

# Calculate PDF for the fitted normal distribution
xmin = df['data1'].min()
xmax = df['data1'].max()
x = np.linspace(xmin, xmax, 100)
p_normal = norm.pdf(x, mu_normal, std_normal)

# Calculate PDF for the fitted exponential distribution
p_exponential = expon.pdf(x, loc_exponential, scale_exponential)

# Define bin sizes
bin_sizes = [5, 10, 20, 25, 50]

# Plot histograms with different bin sizes
plt.figure(figsize=(12, 8))

for i, bins in enumerate(bin_sizes):
    plt.subplot(2, 3, i+1)
    plt.hist(df['data1'], bins=bins, density=True, color='red', edgecolor='black', alpha=0.6, label='Histogram')
    plt.plot(x, p_normal, 'k', linewidth=2, label='Fitted Normal PDF')
    plt.plot(x, p_exponential, 'b--', linewidth=2, label='Fitted Exponential PDF')
    plt.title(f'Bin size = {bins}')
    plt.xlabel('Data 1')
    plt.ylabel('Density')
    plt.legend()

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()

# Display fitted parameters
print("Fitted Parameters:")
print(f"Normal Distribution:")
print(f"  - Estimated mean (mu): {mu_normal:.2f}")
print(f"  - Estimated standard deviation (sigma): {std_normal:.2f}")
print(f"Exponential Distribution:")
print(f"  - Estimated location (loc): {loc_exponential:.2f}")
print(f"  - Estimated scale (scale): {scale_exponential:.2f}")




