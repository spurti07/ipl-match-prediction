import matplotlib.pyplot as plt
import pandas as pd

# Sample data (replace with your actual IPL data)
data = {
    'Season': list(range(2008, 2025)),
    'Auction_Spend_Crores': [55, 60, 75, 65, 80, 90, 100, 110, 120, 130, 135, 140, 150, 155, 160, 170, 180],
    'Playoff_Appearance': [0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Auction Spend (left y-axis)
ax1.plot(df['Season'], df['Auction_Spend_Crores'],
         color='#19b6d6', marker='o', linewidth=2, label='Spend (₹ cr)')
ax1.set_xlabel('Season')
ax1.set_ylabel('Spend (₹ cr)', color='#19b6d6')
ax1.tick_params(axis='y', labelcolor='#19b6d6')

# Plot Playoff Appearance (right y-axis)
ax2 = ax1.twinx()
ax2.plot(df['Season'], df['Playoff_Appearance'],
         color='#ffbb89', marker='s', linestyle='--', linewidth=2, label='Playoff')
ax2.set_ylabel('Playoff', color='#ffbb89')
ax2.tick_params(axis='y', labelcolor='#ffbb89')
ax2.set_yticks([0, 1])

# Title and legends
plt.title('IPL Spend & Playoff by Season')
fig.tight_layout()
plt.show()
