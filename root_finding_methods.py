"""
Root-finding methods for identifying intersection points between two functions.

This module implements numerical techniques such as bisection and
Newton-Raphson to approximate intersection points within a given interval.
"""

import numpy as np
from collections.abc import Iterable

class RootFindingMethods:
    def intersections(self, f1: callable, f2: callable, a: float, b: float, maxerr=0.001) -> Iterable:
        """
        Finds approximate intersection points between two functions f1 and f2
        within the interval [a, b].
        
        Parameters
        ----------
        f1, f2 : callable
            Functions whose intersections are to be computed.
        a, b : float
            Interval bounds.
        maxerr : float
            Maximum allowed error.
        
        Returns
        -------
        Iterable
            Approximate intersection points.
        """
        intersections_list = []
        call_intersect_func = self.intersect_func(f1, f2)
        numbers_between_a_b = np.linspace(a, b, 1000)
        num = 0
        while num < len(numbers_between_a_b) - 1:
            if numbers_between_a_b[num] != None:
                check = self.check_func(numbers_between_a_b[num], numbers_between_a_b[num + 1], call_intersect_func,
                                        maxerr,intersections_list)
            if check != None:
                self.newton_raphson_func(check, numbers_between_a_b[num], numbers_between_a_b[num + 1],
                                         call_intersect_func, maxerr, intersections_list)
                num += 1
            else:
                num += 1
        return intersections_list

    def intersect_func(self, f1: callable, f2: callable):
        return lambda x: f1(x) - f2(x)

    def check_func(self, left, right, call_intersect_func, maxerr,list):
        if call_intersect_func(left) == 0:
            list.append(left)
            return
        if call_intersect_func(right) == 0:
            list.append(right)
            return
        if (call_intersect_func(left) * call_intersect_func(right)) > 0:
            return
        else:
            bisection = self.bisection_func(left, right, call_intersect_func, maxerr)
            return bisection

    def bisection_func(self, left, right, call_intersect_func, maxerr):
        ans = left
        maximum = (left + right) / 2
        for i in range(15):
            ans = (left + right) / 2
            if ans > maximum:
                maximum = ans
            if call_intersect_func(ans) == 0.0 or abs(call_intersect_func(ans)) < maxerr:
                return ans
            if call_intersect_func(left) * call_intersect_func(ans) > 0:
                left = ans
            else:
                right = ans
        return


    def regula_falsi_func(self, f, left, right, maxerr=0.001):
        while abs(right - left) > maxerr:
            ans = (left * f(right) - right * f(left)) / (f(right) - f(left))
            if f(left) * f(right) < 0:
                right = ans
            else:
                left = ans
        return ans

    def secant_func(self, f, left, right, maxerr = 0.001):
        while abs(right - left) > maxerr:
            x = right - f(right) * (right - left) / (f(right) - f(left))
            left = right
            right = x
        return right

    def newton_raphson_func(self, root, left, right, call_intersect_func, maxerr, list):
        r = root
        small_num = 0.000000000001
        derive = (call_intersect_func(r + small_num) / small_num) - (call_intersect_func(r) / small_num)
        for i in range(15):
            e = call_intersect_func(r) / derive
            r = r - e
            derive = (call_intersect_func(r + small_num) / small_num) - (call_intersect_func(r) / small_num)
        if r in list:
            return
        else:
            list.append(r)
