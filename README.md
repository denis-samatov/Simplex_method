# Optimization Problem Solver

This repository contains Python code that demonstrates the solution of a linear programming optimization problem using both the SciPy library and a manual implementation of the simplex method.

## Table of Contents
- [Optimization Problem Solver](#optimization-problem-solver)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Loading Libraries](#loading-libraries)
  - [Building a Task Plot](#building-a-task-plot)
  - [Implementation with SciPy](#implementation-with-scipy)
  - [Result Images](#result-images)
  - [Manual Implementation](#manual-implementation)
  - [Result Images for Manual Implementation](#result-images-for-manual-implementation)
  - [Usage](#usage)
## Introduction

This repository provides a comprehensive solution for linear programming optimization problems using two methods:
1. **SciPy library**: A powerful and widely used library for scientific computing.
2. **Manual Simplex Method**: An algorithmic approach to solving linear programming problems.

The project includes code to set up the optimization problem, visualize it, and solve it using both methods.

## Loading Libraries

The code begins by installing required libraries and importing them for later use. The libraries include `scipy`, `icecream`, `seaborn`, `numpy`, `math`, `pandas`, and `matplotlib`.

```python
%pip install scipy icecream

import seaborn as sns
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

from scipy.optimize import linprog
from icecream import ic
```

## Building a Task Plot

A plot is generated to visualize the optimization problem. This plot illustrates the constraints and objective function of the problem.

![Task Plot](https://github.com/denis-samatov/Simplex_method/blob/main/img_1.png)

## Implementation with SciPy

The SciPy library is used to solve the linear programming problem. The code sets up the objective function and constraints, and then calls the `linprog` function to find the optimal solution.

```python
# Objective function coefficients
obj = [-1, -2]

# Coefficients for the inequality constraints
left_side_ineq = [[ 2,  1],  # Red constraint left side
                  [-4,  5],  # Blue constraint left side
                  [ 1, -2]]  # Yellow constraint left side

# Right-hand side of the inequality constraints
right_side_ineq = [20, 10, 2]

# Coefficients for the equality constraint
left_side_eq = [[-1, 5]]  # Green constraint left side

# Right-hand side of the equality constraint
right_side_eq = [15]

# Bounds for each variable
bnd = [(0, float("inf")),  # Bounds of x
       (0, float("inf"))]  # Bounds of y

opt_ans = linprog(c=obj, A_ub=left_side_ineq, b_ub=right_side_ineq,
                  A_eq=left_side_eq, b_eq=right_side_eq, bounds=bnd,
                  method="revised simplex")

opt_ans
```

## Result Images

After obtaining the solution with SciPy, the code generates a plot to visualize the constraints, objective function, and the optimal solution point.

![SciPy Result](https://github.com/denis-samatov/Simplex_method/blob/main/img_2.png)

## Manual Implementation

The code provides a manual implementation of the simplex method to solve the same linear programming problem. The simplex method functions are defined along with a main function `simplex` that orchestrates the process.

```python
# Manual Implementation
def simplex(c, A, b):
    # Implement the simplex method
    pass

x, y = simplex(c, A, b)
```

## Result Images for Manual Implementation

Finally, the code generates a plot to visualize the constraints, objective function, and the optimal solution point obtained through the manual implementation of the simplex method.

![Manual Simplex Result](https://github.com/denis-samatov/Simplex_method/blob/main/img_3.png)

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/denis-samatov/Simplex_method.git
   cd Simplex_method
   ```
