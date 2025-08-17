import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Example data (replace with your actual values)
teams = ['CSK', 'DC', 'KKR', 'MI', 'PBKS', 'RCB', 'RR']
championships = [0, 1, 2, 5, 0, 0, 1]
retention_percent = [75, 55, 60, 80, 50, 65, 58]

# Create a DataFrame with zeros
heatmap_data = pd.DataFrame(0, index=teams, columns=range(6))

# Fill in retention percentages at the correct championship count for each team
for team, champ, ret in zip(teams, championships, retention_percent):
    if champ < 6:  # To avoid index error if a team has more than 5 championships
        heatmap_data.at[team, champ] = ret

plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', cbar_kws={'label': 'Retention %'}, linewidths=0.5)
plt.title('Heatmap: Retention % vs. Championships')
plt.xlabel('Championships')
plt.ylabel('Team')
plt.tight_layout()
plt.show()
