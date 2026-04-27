# Numerical Methods in Python

A modular Python implementation of core numerical methods, designed as a reusable mini-library.

---

## Features

- Cubic spline interpolation
- Root finding (Bisection, Newton-Raphson, Secant, Regula Falsi)
- Numerical integration (Simpson’s Rule)
- Least squares fitting for noisy data
- Shape reconstruction and area estimation from sampled points
- Utility decorators for timing, noise injection, and constraints

---

## Project Structure
```
numerical-methods-python/
├── cubic_spline_interpolation.py
├── root_finding_methods.py
├── numerical_integration.py
├── least_squares_fitting.py
├── shape_area_estimation.py
├── sample_functions.py
├── function_utils.py
└── README.md
```
---

## Modules Overview

### Cubic Spline Interpolation
Approximates a function over an interval using piecewise cubic polynomials, ensuring smoothness and continuity.

### Root Finding Methods
Finds intersection points between two functions using:
- Bisection method
- Newton-Raphson refinement
- Secant and Regula Falsi (optional helpers)

### Numerical Integration
Implements Simpson’s Rule to approximate definite integrals and compute area between two functions.

### Least Squares Fitting
Fits a polynomial to noisy data by minimizing mean squared error using linear algebra.

### Shape Area Estimation
Reconstructs a shape from noisy sampled points using clustering (KMeans) and estimates its area.

---
