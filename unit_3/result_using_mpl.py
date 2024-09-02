'''import matplotlib.pyplot as mptl
import numpy as np
pooja=[521,497,512,508]
mansi=[493,518,518,543]
viral=[509,519,537,492]

mptl.plot(pooja)
mptl.plot(mansi)
mptl.plot(viral)
mptl.show()'''

'''
# 1.example
import matplotlib.pyplot as plt  # Importing the matplotlib library

# Data to plot
x = [1, 2, 3, 4, 5]  # X-axis values
y = [2, 3, 5, 7, 11]  # Y-axis values

# Create a plot
plt.plot(x, y, label='Line plot')  # Plot data and add a label

# Add title and labels
plt.title('Simple Line Plot')
plt.xlabel('X values')
plt.ylabel('Y values')

# Add a legend
plt.legend()

# Show the plot
plt.show()

'''

'''
# 2.example
'''
import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 2, 8]
data = np.random.randn(1000)

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1: Line Plot
axs[0, 0].plot(x, y, label='Sine Wave', color='b', linestyle='-')
axs[0, 0].plot(x, y2, label='Cosine Wave', color='r', linestyle='--')
axs[0, 0].set_title('Line Plot')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')
axs[0, 0].grid(True)
axs[0, 0].legend()

# Plot 2: Scatter Plot
axs[0, 1].scatter(x, y, c=y, cmap='viridis', alpha=0.7)
axs[0, 1].set_title('Scatter Plot')
axs[0, 1].set_xlabel('X-axis')
axs[0, 1].set_ylabel('Y-axis')
axs[0, 1].grid(True)

# Plot 3: Bar Chart
axs[1, 0].bar(categories, values, color='cyan', edgecolor='black')
axs[1, 0].set_title('Bar Chart')
axs[1, 0].set_xlabel('Categories')
axs[1, 0].set_ylabel('Values')
axs[1, 0].grid(axis='y', linestyle='--')

# Plot 4: Histogram
axs[1, 1].hist(data, bins=30, color='magenta', edgecolor='black')
axs[1, 1].set_title('Histogram')
axs[1, 1].set_xlabel('Data Values')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
