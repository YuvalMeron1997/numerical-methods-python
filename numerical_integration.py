"""
Numerical integration and area computation methods.

This module implements Simpson's rule for numerical integration
and computes the area between two functions by identifying their
intersection points.
"""

import numpy as np
from root_finding_methods import RootFindingMethods


class NumericalIntegration:
    def integrate(self, f: callable, a: float, b: float, n: int) -> np.float32:
        """
        Numerically integrates a function f over the interval [a, b]
        using a limited number of evaluation points.

        Parameters
        ----------
        f : callable. it is the given function
        a : float
            beginning of the integration range.
        b : float
            end of the integration range.
        n : int
            maximal number of points to use.

        Returns
        -------
        np.float32
            Approximate integral value.
        """
        make_integral = self.simpson(a, b, f, n)
        result = np.float32(make_integral)
        return result


    def simpson(self, left, right, function, max_num): #func that finds integral of func between a and b
        if max_num % 2 == 0:
            max_num = (max_num-1)
        h = (right - left) / (max_num-1)
        f0 = 0
        f1 = 0
        f2 = function(right) + function(left)
        for i in range(1, max_num-1):
            x = left + i*h
            if i % 2 == 0:
                f0 += function(x) #even_num
            else:
                f1 += function(x) #odd_num
        return (h / 3) * (2*f0 + 4*f1 + f2)

    def areabetween(self, f1: callable, f2: callable) -> np.float32:
        """
        Finds the area enclosed between two functions. This method finds 
        all intersection points between the two functions to work correctly. 
        
        Example: https://www.wolframalpha.com/input/?i=area+between+the+curves+y%3D1-2x%5E2%2Bx%5E3+and+y%3Dx

        Note, there is no such thing as negative area. 
        
        In order to find the enclosed area the given functions must intersect 
        in at least two points. If the functions do not intersect or intersect 
        in less than two points this function returns NaN.  
        This function may not work correctly if there is infinite number of 
        intersection points. 
        

        Parameters
        ----------
        f1,f2 : callable. These are the given functions

        Returns
        -------
        np.float32
            The area between function and the X axis

        """

        abs_func = self.abs_intersect_function(f1, f2)
        find = self.find_intersection_f(f1, f2)

        area_between_functions = 0
        num_of_points = len(find)
        for i in range(num_of_points-1):
            area_between_functions += self.integrate(abs_func, find[i], find[i+1], 100)
        result = np.float32(area_between_functions)

        return result

    def abs_intersect_function(self, f1, f2): #surface must be positive
        return lambda x: abs(f1(x) - f2(x))

    def find_intersection_f(self, f1, f2): #find roots
        root_finder = RootFindingMethods()
        find = root_finder.intersections(f1, f2, 1, 100) #call the function from assignment2 that find roots
        return find
