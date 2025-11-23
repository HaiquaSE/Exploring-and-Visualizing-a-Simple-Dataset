# Learn how to load, inspect, and visualize a dataset to understand data trends and distributions.
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset
df = sns.load_dataset("iris")
print(df.head)

# print shape, column names, and the first few rows using .head()
print("Shape:", df.shape)
print("\nColumn Name",df.columns.tolist())
print("\nFirst 5 Rows", df.head())

# Use .info() and .describe() for summary statistics.
print("\nInfo:" , df.info())
print("\nSummary Statistics" , df.describe())

# Create a scatter plot to show relationships between features.
plt.figure(figsize = (6 , 4))
plt.scatter(df["sepal_length"], df["sepal_width"])
plt.xlabel ("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Scatter Plot: Sepal Length vs Sepal Width")
plt.show()

# Use histograms to show value distributions.
df.hist(figsize = (10 , 8))
plt.suptitle("Feature Distribyution" , fontsize = 12)
plt.show()