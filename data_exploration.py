import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset
iris = sns.load_dataset('iris')

# Check for missing values
print(iris.isnull().sum())

# Display basic statistics
print(iris.describe())

# Display data types
print(iris.dtypes)

# Histogram for each feature
iris.hist(figsize=(10, 8))
plt.suptitle('Histograms of Iris Features')
plt.show()

# Scatter plot
sns.pairplot(iris, hue='species')
plt.suptitle('Scatter plot of Iris Features', y=1.02)
plt.show()

# Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris)
plt.title('Box plot of Iris Features')
plt.show()
