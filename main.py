# Eric Michael Hicks 2020
# Data analysis tool used to classify three different species of Iris flowers.
# Goal: Use the morphological data to derive a quantifiable way to classify the flowers.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Aesthetics
sns.set_style("darkgrid")

# Select column names
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

# Read the data
iris_data = pd.read_csv("iris.data", header=None)

# Set column names for indexing purposes
iris_data.columns = column_names

# Separate the data by species
iris_setosa = iris_data.loc[iris_data["species"] == "Iris-setosa"]
iris_versicolor = iris_data.loc[iris_data["species"] == "Iris-versicolor"]
iris_virginica = iris_data.loc[iris_data["species"] == "Iris-virginica"]

# Add data to the diagram
# sns.FacetGrid(iris_data,hue="species",height=3).map(sns.distplot,"petal_length").add_legend()
# sns.FacetGrid(iris_data,hue="species",height=3).map(sns.distplot,"petal_width").add_legend()
# sns.FacetGrid(iris_data,hue="species",height=3).map(sns.distplot,"sepal_length").add_legend()
# sns.FacetGrid(iris_data,hue="species",height=3).map(sns.distplot,"sepal_width").add_legend()

# sns.relplot(x="petal_width", y="petal_length", data=iris_data, hue="species")

sns.pairplot(iris_data, hue="species")

plt.show()

