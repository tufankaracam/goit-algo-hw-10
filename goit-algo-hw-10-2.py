import scipy.integrate as spi
import numpy as np


def f(x):
    return x ** 2


# Monte Carlo
a = 0  # Lower bound
b = 2  # Upper bound
n = 1000000  # Number of random samples

x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, f(b), n)

points_under_curve = y_random < f(x_random)
points_under_curve_sum = np.sum(points_under_curve)
integral_monte_carlo = (points_under_curve_sum / n) * (b - a) * f(b)

# Integral
result_quad, error_quad = spi.quad(f, a, b)

# Diff
print(f'Integral : {result_quad}')
print(f'Monte Carlo : {integral_monte_carlo}')
print(f'Diff : {result_quad-integral_monte_carlo}')
