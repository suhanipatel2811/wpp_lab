import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial function, e.g., f(x) = x^3 - 6x^2 + 11x - 6
def f(x):
    return x**3 - 6*x**2 + 11*x - 6

# Step 1: Randomly find initial valid interval [a, b] such that f(a)*f(b) < 0
def find_initial_interval(max_trials=1000, lower=-10, upper=10):
    for _ in range(max_trials):
        a = np.random.uniform(lower, upper)
        b = np.random.uniform(lower, upper)
        if a > b:
            a, b = b, a
        if f(a) * f(b) < 0:
            return a, b
    raise ValueError("Couldn't find valid initial interval.")

# Step 2: Bisection Method Implementation
def bisection_method(a, b, tol=1e-6, max_iter=100):
    iterations = []
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        iterations.append((a, b, c, fc))
        
        if abs(fc) < tol or (b - a) / 2 < tol:
            break
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return np.array(iterations)

# Step 3: Visualize the iterations
def plot_bisection(iterations):
    x_vals = np.linspace(-1, 5, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.axhline(0, color='black', linestyle='--')

    # Plot the bisection steps
    for i, (a, b, c, fc) in enumerate(iterations):
        plt.plot(c, fc, 'ro')
        plt.vlines([a, b], min(y_vals), max(y_vals), colors='gray', linestyles='dotted', alpha=0.3)

    plt.title("Bisection Method Root Finding Process")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the whole process
a, b = find_initial_interval()
iterations = bisection_method(a, b)
print("Final approximation of root:", iterations[-1, 2])
print("Stored iteration data (a, b, c, f(c)):\n", iterations)

# Plot the result
plot_bisection(iterations)
