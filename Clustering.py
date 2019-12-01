
# 3. Find Similar Wines!

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import random
from clustering_lib import kmeans
#matplotlib inline


data=pd.read_csv('wine.data',header=None)
data.columns=['class','Alcohol','Malic_acid','Ash','Alcalinity_of_ash','Magnesium','Total_phenols','Flavanoids','Nonflavanoid_phenols','Proanthocyanins','Color_intensity','Hue','OD280/OD315_of_diluted_wines','Proline']
#data= data.drop('class', 1)
#data= data.drop(columns=[0])
data.head()

# Using K means FUnction

X = data[['Alcohol','Color_intensity']]
df=kmeans(X)
#print (df)


#______________________________________
# Calculating the sum of the attributes
df_sum=df.groupby(["cluster"]).sum()
df_sum

# Counting the number of members in the clusters
df_count=df.groupby(["cluster"]).count()
df_count

# Clculating the values of the centroids
centroids=df_sum.iloc[0:3]/df_count.iloc[0:3,0:2]
#print (centroids)

# Plot

colors = ["red","green","blue","black"]
plt.scatter(df['Alcohol'],df["Color_intensity"],marker='.', s=20, linewidths=5)

# Cluster Plot

df['subset'] = np.select([df.cluster==1, df.cluster==2, df.cluster==3],
                         ['Cluster 1', 'Cluster 2', 'Cluster 3'])
for color, label in zip('bgrm', ['Cluster 1', 'Cluster 2', 'Cluster 3']):
    subset = df[df.subset == label]
    plt.scatter(subset.Alcohol, subset.Color_intensity, s=50, c=color, label=str(label))
plt.scatter(centroids["Alcohol"],centroids["Color_intensity"],c="black",s=200,linewidth=1,marker="*", label="centroids")
plt.legend()


## Retrieveing Data again

#data= data.drop('class', axis=1)

Y = data[['Alcohol','Magnesium','Flavanoids']]

df=kmeans(Y)

# Creating the dataset with each object allocated to a cluster
df.head()

#### Calculating centroids

# Calculating the sum of the attributes
df_sum=df.groupby(["cluster"]).sum()
df_sum

# Counting the number of members in the clusters
df_count=df.groupby(["cluster"]).count()
df_count

# Calculating the values of the centroids
centroids=df_sum.iloc[0:3]/df_count.iloc[0:3,0:3]

#plot
colors = ["red","green","blue","black"]

plt.scatter(df['Magnesium'],df["Alcohol"],df['Flavanoids'],marker='.', linewidths=5)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot

df['subset'] = np.select([df.cluster==1, df.cluster==2, df.cluster==3],
                         ['Cluster 1', 'Cluster 2', 'Cluster 3'])


# Plot
fig = plt.figure()
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 6
fig_size[1] = 4


for color, label in zip('bgrm', ['Cluster 1', 'Cluster 2', 'Cluster 3']):
    subset = df[df.subset == label]
    plt.scatter(subset.Alcohol,subset.Magnesium,subset.Flavanoids,c=color, label=str(label))
plt.scatter(centroids["Alcohol"],centroids["Magnesium"],centroids["Flavanoids"],marker='*',c="black",label="Centroids")
plt.legend()


#3d Plot

from mpl_toolkits.mplot3d import Axes3D
plt.clf()
fig = plt.figure(figsize=(8,6))
ax = Axes3D(fig, elev=-150, azim=210)
for i in range(0,4):
    ax.scatter3D(df[df.cluster == i]['Alcohol'],
                df[df.cluster == i]['Magnesium'],
                df[df.cluster == i]['Flavanoids'], s=100, linewidth=5)
ax.set_xlabel("Alcohol")
ax.set_ylabel("Magnesium")
ax.set_zlabel("Flavanoids")
fig.show()

