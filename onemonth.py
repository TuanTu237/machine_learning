import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
    [2, 3],
    [2, 4],
    [2, 24],
    [5, 1]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:, 0], points[:, 1])

for simplex in hull_points:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

plt.show()
