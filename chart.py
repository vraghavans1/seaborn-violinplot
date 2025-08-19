import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducible results
np.random.seed(42)

# Generate realistic synthetic customer support data
def generate_support_data():
    """Generate realistic customer support response time data"""
    
    # Define support channels with different response time characteristics
    channels = ['Email', 'Phone', 'Chat', 'Social Media']
    data = []
    
    # Email: Generally slower, higher variance (business hours dependency)
    email_times = np.concatenate([
        np.random.gamma(shape=3, scale=8, size=150),  # Main distribution
        np.random.gamma(shape=1.5, scale=20, size=50)  # Some outliers
    ])
    
    # Phone: Faster, more consistent (immediate response expected)
    phone_times = np.concatenate([
        np.random.gamma(shape=2, scale=2, size=180),
        np.random.gamma(shape=1, scale=8, size=20)  # Few longer calls
    ])
    
    # Chat: Fast but with some variation (availability dependent)
    chat_times = np.concatenate([
        np.random.gamma(shape=1.5, scale=3, size=160),
        np.random.gamma(shape=2, scale=12, size=40)  # Peak hour delays
    ])
    
    # Social Media: Mixed response times (monitoring frequency dependent)
    social_times = np.concatenate([
        np.random.gamma(shape=2, scale=6, size=120),
        np.random.gamma(shape=1, scale=15, size=80)  # Delayed responses
    ])
    
    # Combine all data into DataFrame
    all_times = [email_times, phone_times, chat_times, social_times]
    all_channels = [channels[i] for i, times in enumerate(all_times) for _ in times]
    all_response_times = np.concatenate(all_times)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Support_Channel': all_channels,
        'Response_Time_Hours': all_response_times
    })
    
    # Cap extremely high outliers for better visualization
    df['Response_Time_Hours'] = np.clip(df['Response_Time_Hours'], 0, 72)
    
    return df

# Generate the data
support_data = generate_support_data()

# Set up the plot style and context
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=1.1)

# Create figure with specified size for 512x512 output
plt.figure(figsize=(8, 8))

# Create the violinplot
violin_plot = sns.violinplot(
    data=support_data,
    x='Support_Channel',
    y='Response_Time_Hours',
    hue='Support_Channel',  # Add hue to fix deprecation warning
    palette='Set2',
    inner='box',  # Show box plot inside violin
    linewidth=1.5,
    legend=False  # Hide legend since it's redundant with x-axis
)

# Customize the plot
plt.title('Customer Support Response Time Distribution\nby Support Channel', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Support Channel', fontsize=14, fontweight='semibold')
plt.ylabel('Response Time (Hours)', fontsize=14, fontweight='semibold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
plt.grid(True, alpha=0.3, axis='y')

# Customize y-axis to show meaningful ranges
plt.ylim(0, max(support_data['Response_Time_Hours']) * 1.1)

# Add subtle background color
plt.gca().set_facecolor('#fafafa')

# Improve layout to prevent label cutoff
plt.tight_layout()

# Save the chart with exact specifications
plt.savefig('chart.png', dpi=64, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

# Resize to exactly 512x512 pixels as required
from PIL import Image
img = Image.open('chart.png')
img_resized = img.resize((512, 512), Image.Resampling.LANCZOS)
img_resized.save('chart.png')

# Display summary statistics
print("=== Customer Support Response Time Analysis ===")
print("\nSummary Statistics by Channel:")
summary_stats = support_data.groupby('Support_Channel')['Response_Time_Hours'].agg([
    'count', 'mean', 'median', 'std', 'min', 'max'
]).round(2)
print(summary_stats)

print(f"\nVisualization saved as 'chart.png' with dimensions 512x512 pixels")
print("Chart successfully generated for Casper Hessel's customer analytics project")

# Show the plot
plt.show()
