"""
Cubic spline interpolation implementation.

This module provides a method to interpolate a given function
over a specified interval using a limited number of points.
The implementation focuses on balancing accuracy and efficiency.
"""

import numpy as np

class CubicSplineInterpolation:

    def interpolate(self, f: callable, a: float, b: float, n: int) -> callable:
        """
        Interpolates a function f over the interval [a, b] using at most n sample points.
    
        The implementation constructs a cubic spline approximation to achieve a balance
        between accuracy and computational efficiency.
    
        Parameters
        ----------
        f : callable
            Function to interpolate.
        a : float
            Start of the interval.
        b : float
            End of the interval.
        n : int
            Maximum number of sample points.
    
        Returns
        -------
        callable
            Interpolating function.
        """
        segments_between_a_b = np.linspace(a, b, n) #segmets
        points = np.empty([n, 2]) #matrix: [0. 0.] 2 columns, n rows
        i = 0
        while i < n:
            x_val = segments_between_a_b[i]
            points[i] = [x_val, f(x_val)] #array of n arrays of points[x,y]
            i += 1
        A, B = self.build_vec_matrix(points)
        d = {}
        for i in range(len(points) - 1):
            d[(points[i][0], points[i][1])] = self.get_cubic(points[i], A[i], B[i], points[i + 1])
        dict_ans = d
        result = lambda x: self.find_x(x, dict_ans)
        return result

    def build_vec_matrix(self, points):
        n = len(points) - 1
        C = 4 * np.identity(n)
        np.fill_diagonal(C[1:], 1)
        np.fill_diagonal(C[:, 1:], 1)
        C[0, 0] = 2
        C[n - 1, n - 1] = 7
        C[n - 1, n - 2] = 2
        down = list(np.diag(C, k=-1))
        middle = list(np.diag(C))
        up = list(np.diag(C, k=1))
        vec = [2 * (2 * points[i] + points[i + 1]) for i in range(n)]
        vec[0] = points[0] + 2 * points[1]
        vec[n - 1] = 8 * points[n - 1] + points[n]
        return self.thomas(down,middle,up,vec, points)



    def thomas_algorithm(self, down, middle, up, vec, points):
        n = len(middle)
        A = [0] * n
        for i in range(1,n):
            divide = down[i-1] / middle[i-1]
            middle[i] = middle[i] - up[i-1] * divide
            vec[i] = vec[i] - vec[i - 1] * divide
        A[n-1] = vec[n-1] / middle[n-1]
        for i in range(n - 2, -1, -1):
            A[i] = (vec[i] - up[i] * A[i+1]) / middle[i]
        B = [0] * n
        for i in range(n - 1):
            B[i] = 2 * points[i + 1][1] - A[i + 1]
        B[n - 1] = (A[n - 1] + points[n][1]) / 2
        return A, B


    def get_cubic(self, a, b, c, d):
        return lambda t: np.power(1 - t, 3) * a + 3 * np.power(1 - t, 2) * t * b + 3 * (1 - t) * np.power(t, 2) * c + np.power(t, 3) * d


    def find_x(self, x, dict_ans):
        s = (0,0)
        e = (0,0)
        for key in dict_ans.keys():
            if x > key[0]:
                s = key
            else:
                e = key
                break
        res = dict_ans[s]((x-s[0]) / (e[0]-s[0]))[1]
        return res
