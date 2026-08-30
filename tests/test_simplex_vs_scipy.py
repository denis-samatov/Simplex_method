"""Checks the manual simplex implementation against scipy.optimize.linprog
on the repo's reference LP, using the exact formulation the notebook's own
linprog() call uses:

minimize   8x + 6y
subject to  x +  y  = 300   (equality)
            x + 2y <= 375
            x, y >= 0
"""

import numpy as np
import pytest
from scipy.optimize import linprog

from simplex_solver import simplex

C = [8.0, 6.0, 0.0]
A = [[1.0, 1.0, 0.0], [1.0, 2.0, 0.0]]
B = [300.0, 375.0]

SCIPY_RESULT = linprog(
    c=[8, 6],
    A_ub=[[1, 2]],
    b_ub=[375],
    A_eq=[[1, 1]],
    b_eq=[300],
    bounds=[(0, None), (0, None)],
)


def test_scipy_reference_solves_the_problem():
    # Sanity check on our own SciPy call, independent of simplex_solver.
    assert SCIPY_RESULT.success
    assert SCIPY_RESULT.x == pytest.approx([225, 75], abs=1e-6)
    assert SCIPY_RESULT.fun == pytest.approx(2250, abs=1e-6)


def test_manual_simplex_solution_is_feasible():
    x, y, _ = simplex(C, A, B)

    assert x >= -1e-9
    assert y >= -1e-9
    assert x + y == pytest.approx(300, abs=1e-6)
    assert x + 2 * y <= 375 + 1e-9


def test_manual_simplex_matches_scipy_optimum():
    x, y, _ = simplex(C, A, B)

    assert np.array([x, y]) == pytest.approx(SCIPY_RESULT.x, abs=1e-6)
