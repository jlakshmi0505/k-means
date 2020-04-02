# k-means
k-means Implentation from Scratch in Python

Implement k-Means
Create a python-based implementation of the k-means algorithm.

This implementation must be a subclass of cluster.py, available here (Links to an external site.). As such, it must implement two member functions: __init__(...) and fit(...), as described below.

__init__(...) must allow the class’ users to set the algorithm’s hyperparameters: k, which is the target number of cluster centroids, and max_iterations, which is maximum number of times to execute the convergence attempt (repeat loop in the above Background section). The default values are required to be k = 5 and max_iterations = 100.
 fit(...) must accept one parameter  X, where X is a list (not columns of a Dataframe) of n instances in d dimensions (features) which describe the n instances. A successful call to the fit(...) function must return the following two items, in order:
A list (of length n) of the cluster hypotheses, one for each instance.
A list (of length at most k) containing lists (each of length d) of the cluster centroids’ values.
For example, if the input (X) contains the following values in 2-dimensional space:

[ [0, 0], [2, 2], [0, 2], [2, 0], [10, 10], [8, 8], [10, 8], [8, 10] ]

… and k = 2, we expect the centroids should be [1, 1] and [9, 9]. The output of the fit(...) function should be as follows:

[0, 0, 0, 0, 1, 1, 1, 1] — indicating that the first four instances belong to one cluster and the second four belong to a different cluster.
[ [1, 1], [9, 9] ] — the values for the first and second centroid, respectively.
Test the python-based implementation using scikit-learn. Generate clusters using the make_blobs function with the following commands:
from sklearn.datasets.samples_generator import make_blobs
X, cluster_assignments = make_blobs(n_samples=200, centers=4, cluster_std=0.60, random_state=0)
This will generate 200 instances of data points in 2-dimensional space, with each of the instances belonging to one of 4 clusters. The coordinates for the 100 instances are returned as X. The cluster assignments are returned as cluster_assignments. Use X as the parameter to your fit(...) function listed above, and use cluster_assignments to determine whether your implementation’s hypotheses are correct. (Given multiple — 10? — iterations of your implementation with k=4, the values for X from the commands above should generate no errors; however, the values in cluster_assignments may not align to the values from your implementation’s hypotheses.)

Please include your function's sample output from this test input as a .TXT file.
