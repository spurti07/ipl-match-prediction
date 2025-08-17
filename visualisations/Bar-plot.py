import matplotlib.pyplot as plt

# Data for player roles and their ROI
roles = ['Opener', 'Middle-order', 'Finisher', 'Spinner', 'Pace Bowler', 'All-rounder']
roi = [1.6, 2.3, 2.1, 2.7, 1.8, 2.9]
colors = ['#19b6d6', '#ffbb89', '#f7f6d1', '#5c7d8a', '#e1c04e', '#c0392b']

plt.figure(figsize=(10,6))
bars = plt.bar(roles, roi, color=colors)

# Annotate each bar with the ROI value
for bar, value in zip(bars, roi):
    plt.text(bar.get_x() + bar.get_width()/2, value + 0.05, f"{value:.2f}",
             ha='center', va='bottom', fontsize=13, fontweight='bold')

plt.title('IPL Player Role ROI Comparison', fontsize=22, fontweight='bold', pad=20)
plt.xlabel('Role', fontsize=16)
plt.ylabel('ROI', fontsize=16)
plt.ylim(0, 3.2)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
