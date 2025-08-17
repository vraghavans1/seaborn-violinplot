import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
channels = ["Email", "Chat", "Phone", "Social Media"]
data = {
    "Channel": np.random.choice(channels, 400),
    "ResponseTime": np.concatenate([
        np.random.normal(30, 10, 100),   # Email
        np.random.normal(10, 5, 100),    # Chat
        np.random.normal(20, 7, 100),    # Phone
        np.random.normal(15, 6, 100)     # Social Media
    ])
}

df = pd.DataFrame(data)

# Set professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.1)

# Create figure (8x8 inches -> 512x512px at dpi=64)
plt.figure(figsize=(8, 8))

# Create violinplot
sns.violinplot(
    x="Channel",
    y="ResponseTime",
    data=df,
    palette="Set2",
    inner="quartile"
)

# Titles and labels
plt.title("Customer Support Response Time Distribution by Channel", fontsize=14, weight="bold")
plt.xlabel("Support Channel", fontsize=12)
plt.ylabel("Response Time (minutes)", fontsize=12)

# Save chart as 512x512
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
