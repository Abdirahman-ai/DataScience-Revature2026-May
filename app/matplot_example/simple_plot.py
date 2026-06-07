# matplotlib is a data visualization library that lets us make a different types of

# pyplot is matplotlib module that lets us easily create charts

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.plot(x, y, color="forestgreen", linestyle=":", markersize=5)
plt.title("Simple Plot", fontsize=32, fontweight='bold')
plt.xlabel("Months", fontsize=18)
plt.ylabel("Pototoes eaten", fontsize=18)
plt.grid(True, alpha=0.5)

plt.show()

# DOING a bar chart now
types_of_potatoes = ["Russet", "Fingerling", "Yukon Gold"]
potatoes_eaten =  [400, 200, 515]

plt.bar(types_of_potatoes, potatoes_eaten, color=["Saddlebrown", "goldenrod", "peru"])
plt.title("potatoes eaten", fontsize=32, fontweight='bold')
plt.xlabel("types of potatoes"
           "", fontsize=18)
plt.ylabel("Pototoes eaten", fontsize=18)
plt.show()