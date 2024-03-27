import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon, norm, kstest
import pandas as pd

# Load your data
df = pd.read_excel('../data/w6L2.xlsx')

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

# Define bin sizes for histograms
bin_sizes = [5, 10, 20, 25, 50]

# Create subplots for histograms
fig, axs = plt.subplots(1, 5, figsize=(20, 5))

# Plot histograms with different bin sizes and fitted PDFs
for i, bins in enumerate(bin_sizes):
    ax = axs.flatten()[i]
    ax.hist(df['data1'], bins=bins, density=True, color='red', edgecolor='black', alpha=0.6, label='Histogram')
    ax.plot(x, p_normal, 'k', linewidth=2, label='Fitted Normal PDF')
    ax.plot(x, p_exponential, 'g', linewidth=2, label='Fitted Exponential PDF')
    ax.set_title(f'Bin size = {bins}')
    ax.set_xlabel('Data 1')
    ax.set_ylabel('Density')
    ax.legend()

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

# Perform Kolmogorov-Smirnov test for normal distribution
ks_statistic_normal, p_value_normal = kstest(df['data1'], 'norm', args=(mu_normal, std_normal))
print("Kolmogorov-Smirnov Test for Normal Distribution:")
print(f"KS Statistic: {ks_statistic_normal:.4f}")
print(f"P-value: {p_value_normal:.4f}")

# Perform Kolmogorov-Smirnov test for exponential distribution
ks_statistic_exponential, p_value_exponential = kstest(df['data1'], 'expon', args=(loc_exponential, scale_exponential))
print("\nKolmogorov-Smirnov Test for Exponential Distribution:")
print(f"KS Statistic: {ks_statistic_exponential:.4f}")
print(f"P-value: {p_value_exponential:.4f}")

# Define null hypotheses
null_hypothesis_normal = "Null Hypothesis (H0): The data follows a normal distribution."
null_hypothesis_exponential = "Null Hypothesis (H0): The data follows an exponential distribution."

# Interpret results and generate comments
if p_value_normal > 0.05:
    comment_normal = "The data is reasonably consistent with a normal distribution."
else:
    comment_normal = "The data significantly deviates from a normal distribution."

if p_value_exponential > 0.05:
    comment_exponential = "The data is reasonably consistent with an exponential distribution."
else:
    comment_exponential = "The data significantly deviates from an exponential distribution."

# Display results including null hypotheses
print("Comments on Kolmogorov-Smirnov Test Results:")
print("Normal Distribution Test:", comment_normal)
print("  ", null_hypothesis_normal)
print("Exponential Distribution Test:", comment_exponential)
print("  ", null_hypothesis_exponential)
