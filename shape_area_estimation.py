"""
Shape reconstruction and area estimation from noisy samples.

This module fits a contour to sampled points using clustering
and estimates the enclosed area.
"""

import numpy as np
from functionUtils import AbstractShape
from sklearn.cluster import KMeans



class EstimatedShape(AbstractShape):
    def __init__(self, area_1):
        self.a = area_1

    def area(self):
        return self.a

class ShapeAreaEstimation:
    def area(self, contour: callable, maxerr=0.001) -> np.float32:
        """
        Compute the area of the shape with the given contour.

        Parameters
        ----------
        contour : callable
            Same as AbstractShape.contour
        maxerr : TYPE, optional
            The target error of the area computation. The default is 0.001.

        Returns
        -------
        The area of the shape.

        """
        def helper(x):
            points = contour(x)
            num = 0
            for i in range(len(points)):
                num += 0.5 * ((points[i][0] - points[i - 1][0]) * (points[i][1] + points[i - 1][1]))
            return num

        n = 250
        points_0 = helper(n)
        points_1 = helper(int(n*1.3))
        while n < 10000:
            if abs(abs(points_1)-abs(points_0)) / abs(points_1) < maxerr:
                return np.float32(abs(points_1))
            n = int(n*1.3)
            points_0 = points_1
            points_1 = helper(n)
        return np.float32(abs(points_1))


    def fit_shape(self, sample: callable, maxtime: float) -> AbstractShape:
        """
        Build a function that accurately fits the noisy data points sampled from
        some closed shape.

        Parameters
        ----------
        sample : callable.
            An iterable which returns a data point that is near the shape contour.
        maxtime : float
            This function returns after at most maxtime seconds.

        Returns
        -------
        An object extending AbstractShape.
        """
        points = self.find_points(sample)
        shape = self.km(points)
        a = 0
        for i in range(len(shape) - 1):
            a += (shape[i + 1][0] - shape[i][0]) * (((shape[i + 1][1]) + (shape[i][1])) / 2)
        ans = abs(a)
        res = EstimatedShape(ans)
        return res

    def find_points(self, sample):
        points_list = np.array([sample() for i in range(120000)])
        return points_list

    def km(self, points_list):
        kmeans = KMeans(n_clusters=30, random_state=0).fit(points_list)
        shape_contour = kmeans.cluster_centers_
        shape_contour_arr = np.array(shape_contour)
        ans = self.sort_points(shape_contour_arr)
        return ans

    def sort_points(self, points_arr):
        centroid = np.mean(points_arr, axis=0)
        angles = np.arctan2(points_arr[:, 1] - centroid[1], points_arr[:, 0] - centroid[0])
        sorted_indices = np.argsort(angles)
        sorted_points = points_arr[sorted_indices]
        return sorted_points
