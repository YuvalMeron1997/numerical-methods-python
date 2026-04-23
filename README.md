# Numerical Methods in Python

A modular Python implementation of core numerical methods, including interpolation, root finding, numerical integration, optimization, and geometric analysis.

This project was developed as part of a numerical analysis course and structured as a reusable mini-library.

---

## 🚀 Features

- Cubic spline interpolation
- Root finding (Bisection, Newton-Raphson, Secant, Regula Falsi)
- Numerical integration (Simpson’s Rule)
- Least squares fitting for noisy data
- Shape reconstruction and area estimation from sampled points
- Utility decorators for timing, noise injection, and constraints

---

## 📁 Project Structure
```
numerical-methods-python/
│
├── cubic_spline_interpolation.py # Function interpolation using cubic splines
├── root_finding_methods.py # Intersection finding between functions
├── numerical_integration.py # Integration + area between curves
├── least_squares_fitting.py # Polynomial fitting (least squares)
├── shape_area_estimation.py # Shape reconstruction + area estimation
│
├── sample_functions.py # Test functions and shapes
├── function_utils.py # Utilities (decorators, AbstractShape)
│
└── README.md
```
---

## 🧠 Modules Overview

### 🔹 Cubic Spline Interpolation
Approximates a function over an interval using piecewise cubic polynomials, ensuring smoothness and continuity.

### 🔹 Root Finding Methods
Finds intersection points between two functions using:
- Bisection method
- Newton-Raphson refinement
- Secant and Regula Falsi (optional helpers)

### 🔹 Numerical Integration
Implements Simpson’s Rule to approximate definite integrals and compute area between two functions.

### 🔹 Least Squares Fitting
Fits a polynomial to noisy data by minimizing mean squared error using linear algebra.

### 🔹 Shape Area Estimation
Reconstructs a shape from noisy sampled points using clustering (KMeans) and estimates its area.

---

## ⚙️ Utilities

### function_utils.py
Includes:
- `TIMED` – measure execution time
- `DELAYED` – simulate delays
- `NOISY` – inject noise into function outputs
- `FLOAT32` – enforce float32 precision
- `RESTRICT_INVOCATIONS` – limit function calls
- `AbstractShape` – base class for geometric shapes

---
