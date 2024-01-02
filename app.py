import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset
iris = sns.load_dataset("iris")

# Set up the dashboard layout
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))
plt.subplots_adjust(wspace=0.5, hspace=0.5)

# 1. Pie Chart
iris_species_counts = iris['species'].value_counts()
axes[0, 0].pie(iris_species_counts, labels=iris_species_counts.index, autopct='%1.3f%%', startangle=90)
axes[0, 0].set_title('Pie Chart')

# 2. Line Chart
sns.lineplot(data=iris, x='species', y='sepal_width', ax=axes[0, 1])
axes[0, 1].set_title('Line Chart')

# 3. Stacked Bar Chart
sns.barplot(data=iris, x='species', y='petal_length', hue='species', ax=axes[0, 2], estimator=sum)
axes[0, 2].set_title('Stacked Bar Chart')

# 4. Scatter Plot
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', ax=axes[1, 0])
axes[1, 0].set_title('Scatter Plot')

# 5. Heat Map
sns.heatmap(iris.describe()[1:].transpose(), annot=True, cmap='Blues', linewidths=0.5, ax=axes[1, 1])
axes[1, 1].set_title('Heat Map')

# Remove empty subplot
fig.delaxes(axes[1, 2])

# Show the plots
plt.show()
