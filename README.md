# Optimization Problem Solver

This repository contains Python code that demonstrates the solution of a linear programming optimization problem using both the SciPy library and a manual implementation of the simplex method.

## Table of Contents
- [Loading Libraries](#loading-libraries)
- [Task Plot](#building-a-task-plot)
- [Implementation with SciPy](#implementation-with-scipy)
- [Result Images](#result-images)
- [Manual Implementation](#manual-implementation)
- [Result Images for Manual Implementation](#result-images-for-manual-implementation)

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

![image example](https://github.com/denis-samatov/Simplex_method/blob/main/img_1.png)

## Implementation with SciPy
The SciPy library is used to solve the linear programming problem. The code sets up the objective function and constraints, and then calls the `linprog` function to find the optimal solution.

```python
# Implementation with SciPy

opt_ans = linprog(c=obj, A_ub=left_side_ineq, b_ub=right_side_ineq,
                  A_eq=left_side_eq, b_eq=right_side_eq, bounds=bnd,
                  method="revised simplex")

opt_ans
```

## Result Images
After obtaining the solution with SciPy, the code generates a plot to visualize the constraints, objective function, and the optimal solution point.

![image example](https://github.com/denis-samatov/Simplex_method/blob/main/img_2.png)

## Manual Implementation
The code then provides a manual implementation of the simplex method to solve the same linear programming problem. The simplex method functions are defined along with a main function `simplex` that orchestrates the process.

```python
# Manual Implementation

x, y = simplex(c, A, b)
```

## Result Images for Manual Implementation
Finally, the code generates a plot to visualize the constraints, objective function, and the optimal solution point obtained through the manual implementation of the simplex method.

![image example](https://github.com/denis-samatov/Simplex_method/blob/main/img_3.png)

Feel free to use and modify this code for your own linear programming problems.
