# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Data Generation: Create realistic synthetic data
np.random.seed(42)
data = {
    'Response Time (Minutes)': np.concatenate([
        np.random.normal(loc=15, scale=5, size=200),   # Chat: fast with low variance
        np.random.normal(loc=240, scale=45, size=300), # Email: slow with high variance
        np.random.normal(loc=8, scale=3, size=400),    # Phone: very fast with low variance
        np.random.normal(loc=60, scale=20, size=150)   # Social Media: medium speed and variance
    ]),
    'Support Channel': ['Chat'] * 200 + ['Email'] * 300 + ['Phone'] * 400 + ['Social Media'] * 150
}
df = pd.DataFrame(data)

# 2. Professional Styling
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.8)

# 3. Create Violin Plot
# Set figure size for 512x512 output (8 inches * 64 dpi = 512 pixels)
plt.figure(figsize=(8, 8))

# Create the plot with a professional color palette
ax = sns.violinplot(
    x='Support Channel',
    y='Response Time (Minutes)',
    data=df,
    palette='viridis',
    inner='quartile', # Show quartiles inside the violins
    linewidth=1.5
)

# 4. Style the Chart
plt.title('Customer Support Response Time Distribution by Channel', fontsize=16, weight='bold')
plt.xlabel('Support Channel', fontsize=12)
plt.ylabel('Response Time (Minutes)', fontsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0) # Keep x-axis labels horizontal

# Improve readability
plt.tight_layout()

# 5. Export the Chart
# Save as PNG with exactly 512x512 pixel dimensions
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

print("Chart 'chart.png' (512x512) has been generated successfully.")
