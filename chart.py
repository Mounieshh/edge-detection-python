import matplotlib.pyplot as plt

# Sample dataset
categories = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Pears']
values = [10, 20, 30, 40, 50]

# Create the figure and axis
fig, ax = plt.subplots()

# Create the bar chart
ax.bar(categories, values)

# Set the title and labels
ax.set_title('Fruit Sales')
ax.set_xlabel('Fruit Type')
ax.set_ylabel('Sales (units)')

# Show the chart
plt.show()
