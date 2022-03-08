# Assignment: Lab 12a - Act2
# Date: 11/9/2020


################# Imports #################
import numpy as np
import matplotlib.pyplot as plt


################ Functions ################

# Convert the coefficients from strings to ints
def coefficients():
    # Take user input coefficients
    A, B, C, D = input("Enter 4 coefficient values: ").split()
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    return A,B,C,D

#  define the functions: y1-f(x), y2-f'(x), y3-f"(x)
def y1(x):
    return A * x ** 3 + B * x ** 2 + C * x + D
def y2(x):
    return 3 * A * x ** 2 + 2 * B * x + C
def y3(x):
    return 6 * A * x + 2 * B

# Calculate the maximum X and Y values for f(x)
# When using return values: 0 - x,  1 - y
def max_y1(roots):
    max_x = -10000000
    max_y = -10000000
    for r in roots:
        if (y1(r)>max_y):
            max_y = y1(r)
            max_x = r
    return max_x, max_y

# Calculate the minimum X and Y values for f(x)
# When using return values (index numbers): 0 - x,  1 - y
def min_y1(roots):
    max_y = max_y1(roots)[1]
    min_x = 10000000
    min_y = 10000000
    for r in roots:
        if (y1(r) != max_y1):
            min_y = y1(r)
            min_x = r
    return min_x, min_y

# Plot f(x) and format the line
# Plot the max and min values (2) as black dots
def plot_y1(x):
    plt.plot(x, y1(x), "b",  label="f(x)")
    plt.plot(max_y1(roots_y2)[0], max_y1(roots_y2)[1], "ko")
    plt.plot(min_y1(roots_y2)[0], min_y1(roots_y2)[1], "ko")

# Plot f'(x) and format the line
# Plot the max or min value (1) as black dots
def plot_y2(x):
    plt.plot(x, y2(x), "g--", label="f'(x)")
    plt.plot(extrema_x2, extrema_y2, "ko")

# Plot f"(x) and format the line
def plot_y3(x):
    plt.plot(x, y3(x), "r:", label="f''(x)")

# Create the graph - labels, axes, legend
# Plot the functions
def create_graph(x):
    # Plot lines and max&min
    plot_y1(x)
    plot_y2(x)
    plot_y3(x)
    # show the plot and labels
    plt.title("Plots of f(x), f'(x), f''(x) with local max and min")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.legend()
    plt.show()

################ Main Code ################

# Assign return value of coefficient function to A,B,C,D
A,B,C,D = coefficients()

# Create x variable - 100 linearly spaced numbers
x = np.linspace(-5, 5, 50)

# Create roots variables
# roots_y2 = the roots of f'(x) - these will be the max and min of f(x)
roots_y2 = np.roots([3 * A, 2 * B, C])
# root_y3 = the root of f"(x) - this will be the max or min of f'(x)
root_y3 = np.roots([6 * A, 2 * B])

# These are the x and y coordinates of the f'(x) max or min
extrema_x2 = root_y3
extrema_y2 = y2(root_y3)

# Create graph
create_graph(x)
