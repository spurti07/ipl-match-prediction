import matplotlib.pyplot as plt

# Example data (replace with your actual values)
teams = ['PBKS', 'DC', 'RCB', 'KKR', 'MI', 'CSK']
avg_retained = [2.0, 2.5, 4.0, 4.5, 7.2, 7.5]  # x-axis
continuity = [40, 42, 55, 60, 70, 73]           # y-axis
cluster = ['High Churn', 'High Churn', 'Mixed Strgy', 'Mixed Strgy', 'Stable High', 'Stable High']
bubble_size = [700, 700, 900, 900, 1100, 1100]  # Bubble size for visibility

# Color mapping for clusters
colors = {'Stable High': '#6ec6ca', 'Mixed Strgy': '#f7c59f', 'High Churn': '#fbeec1'}
cluster_color = [colors[c] for c in cluster]

plt.figure(figsize=(8,5))
scatter = plt.scatter(avg_retained, continuity, s=bubble_size, c=cluster_color, alpha=0.8, edgecolors='gray')

# Annotate team names
for i, team in enumerate(teams):
    plt.text(avg_retained[i]+0.1, continuity[i]+1, team, fontsize=10, weight='bold')

# Custom legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor=colors['Stable High'], label='Stable High'),
    Patch(facecolor=colors['Mixed Strgy'], label='Mixed Strgy'),
    Patch(facecolor=colors['High Churn'], label='High Churn')
]
plt.legend(handles=legend_elements, title='Cluster', loc='upper center', bbox_to_anchor=(0.5, 1.08), ncol=3)
plt.title('IPL Team Retention and Auction Strategy', 
          fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Avg Retained', fontsize=12)
plt.ylabel('Cont %', fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
