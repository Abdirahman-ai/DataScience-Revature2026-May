# subplots - multiple charts in a single figure

import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [10, 20, 30, 40, 50]
returns = [1, 2, 3, 4, 5]

# Create a figure (The window with our charts) with 1 row and 2 columns of charts
# Figsize() is the size of the figure in inches
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Each ax(axis) is its own chart in the figure
ax1.plot(months, sales, marker="o", color="blue")
ax1.title.set_text("Monthly Sales")
ax1.set_xlabel("Months")
ax1.set_ylabel("Units sold")
ax1.grid(True)

ax2.plot(months, returns,
         marker="x",
         markerfacecolor = "green",
         markeredgecolor="green",
         color="red")
ax2.title.set_text("Monthly Returns")
ax2.set_xlabel("Month")
ax2.set_ylabel("Units Returned")
ax2.grid(True)

plt.tight_layout() # automatically adjusts
plt.show()