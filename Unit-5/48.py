'''48.Write a program to plot line bar histogram and
pie charts using Python. '''

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [10, 15, 12, 20]

students = ["A", "B", "C", "D"]
marks = [60, 70, 80, 90]

# Line Chart
plt.subplot(2, 2, 1)
plt.plot(months, sales, marker='o')
plt.title("Line Chart")

# Bar Chart
plt.subplot(2, 2, 2)
plt.bar(months, sales)
plt.title("Bar Chart")

# Histogram
plt.subplot(2, 2, 3)
plt.hist(marks, bins=5)
plt.title("Histogram")

# Pie Chart
plt.subplot(2, 2, 4)
plt.pie(marks, labels=students)
plt.title("Pie Chart")

plt.show()
