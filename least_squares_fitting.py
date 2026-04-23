"""
Least squares fitting for noisy data.

This module fits a polynomial model to noisy samples of a function
using a least squares approach.
"""

import numpy as np
import time

class LeastSquaresFitting:

    def fit(self, f: callable, a: float, b: float, d: int, maxtime: float) -> callable:
        """
        Fits a polynomial model to noisy samples of a function within [a, b].

        Parameters
        ----------
        f : callable.
            A function which returns an approximate (noisy) Y value given X.
        a: float
            Start of the fitting range
        b: float
            End of the fitting range
        d: int
            The expected degree of a polynomial matching f
        maxtime : float
            This function returns after at most maxtime seconds.

        Returns
        -------
        a function:float->float that fits f between a and b
        """

        start = time.time()
        x_values = []
        y_values = []
        while True:
            if int(time.time()) - int(start) >= (maxtime*0.7):
                break
            else:
                x_value = np.random.uniform(a,b,1)[0]
                y = f(x_value)
                y_values.append(y)
                x_values.append(x_value)


        res_list = self.least_squares(x_values, y_values, d)

        def result(x):
            res = 0
            degree = len(res_list)-1
            for i in range(len(res_list)):
                res += float(np.power(x, degree)) * float(res_list[i])
                degree -= 1
            return res

        return result


    def least_squares(self, x_values, y_values, d):
        A = np.vander(x_values, d+1)
        b = np.array(y_values)
        A_transpose = np.transpose(A)
        A_transpose_A = np.dot(A_transpose, A)
        A_transpose_A_inv = np.linalg.inv(A_transpose_A)
        A_transpose_A_inv_A_transpose = np.dot(A_transpose_A_inv, A_transpose)
        coef = np.dot(A_transpose_A_inv_A_transpose, b)
        return coef
