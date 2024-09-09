import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 4]

# Create figure and subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Line plot
ax1.plot(x, y, label='Sine Wave')
ax1.plot(x, y2, label='Cosine Wave')
ax1.set_title('Line Plot')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.legend()

# Scatter plot
ax2.scatter(x, y, label='Sine Points', color='r')
ax2.scatter(x, y2, label='Cosine Points', color='b')
ax2.set_title('Scatter Plot')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.legend()

# Bar chart
ax3.bar(categories, values, color=['red', 'blue', 'green', 'purple'])
ax3.set_title('Bar Chart')
ax3.set_xlabel('Categories')
ax3.set_ylabel('Values')

# Adjust layout
plt.tight_layout()
plt.show()
