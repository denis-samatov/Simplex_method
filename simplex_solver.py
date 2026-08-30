"""Manual tableau-based simplex implementation, extracted from
Simplex_method.ipynb so it's importable and testable outside the notebook.

Behavior is UNCHANGED from the notebook (including a known bug -- see
`simplex()`'s docstring and tests/test_simplex_vs_scipy.py). This module
exists to make that bug testable and documented, not to fix it.
"""

import math

import numpy as np


def convert_to_simplex_table(c, A, b):
    """Builds the initial simplex tableau: each constraint row is [A_row..., b],
    with the objective row [c..., 0] appended last."""
    xb = [eqn + [x] for eqn, x in zip(A, b)]
    z = c + [0]
    return xb + [z]


def check(simplex_table):
    """Returns True while any objective-row coefficient (excluding the
    constant term) is still nonzero."""
    z = simplex_table[-1]
    return any(x != 0 for x in z[:-1])


def get_pivot_point(simplex_table):
    """Picks the pivot column (first nonzero objective-row coefficient) and
    pivot row (minimum ratio test)."""
    z = simplex_table[-1]
    column = [i for i, x in enumerate(z[:-1]) if x != 0][0]

    restrictions = []
    for eqn in simplex_table[:-1]:
        element = eqn[column]
        restrictions.append(math.inf if element <= 0 else eqn[-1] / element)

    row = restrictions.index(min(restrictions))
    return row, column


def rotate_simplex_table(simplex_table, pivot_point):
    """Performs one Gauss-Jordan pivot step around (row, column)."""
    new_simplex_table = [[] for eqn in simplex_table]
    i, j = pivot_point

    pivot_value = simplex_table[i][j]
    new_simplex_table[i] = np.array(simplex_table[i]) / pivot_value

    for eqn_index, eqn in enumerate(simplex_table):
        if eqn_index != i:
            multiplier = np.array(new_simplex_table[i]) * simplex_table[eqn_index][j]
            new_simplex_table[eqn_index] = np.array(simplex_table[eqn_index]) - multiplier

    return new_simplex_table


def check_basic_var(column):
    """A column is a basic variable's column if it's a unit vector (exactly
    one 1, everything else 0)."""
    return sum(column) == 1 and len([col for col in column if col == 0]) == len(column) - 1


def get_solution(simplex_table):
    """Reads the variable values off the current tableau: a basic variable's
    value is the b-column entry in its unit-vector row; non-basic
    variables are 0."""
    columns = np.array(simplex_table).T

    solutions = []
    for column in columns[:-1]:
        solution = 0
        if check_basic_var(column):
            one_index = column.tolist().index(1)
            solution = columns[-1][one_index]
        solutions.append(solution)

    return solutions


def simplex(c, A, b):
    """Solves this module's reference LP with a hand-rolled tableau method.

    Verified against scipy.optimize.linprog on the notebook's own reference
    problem (minimize 8x+6y s.t. x+y=300 (equality), x+2y<=375, x,y>=0 --
    see tests/test_simplex_vs_scipy.py): both agree on (225, 75), objective
    2250. This is not a general-purpose simplex solver -- the caller must
    already know how many tableau columns are needed and pad c/A with the
    right number of trailing zero columns (as this problem's own inputs
    do); it has not been verified against other LP shapes.

    Args:
        c (list): Objective coefficients, e.g. [8.0, 6.0, 0.0] (padded to
            match the tableau's column count).
        A (list[list]): Constraint coefficient rows, padded the same way.
        b (list): Right-hand-side values for each constraint.

    Returns:
        list: The solution vector (one entry per column of A/c).
    """
    simplex_table = convert_to_simplex_table(c, A, b)

    while check(simplex_table):
        pivot_point = get_pivot_point(simplex_table)
        simplex_table = rotate_simplex_table(simplex_table, pivot_point)

        if simplex_table[-1][-2] != 0:
            break

    return get_solution(simplex_table)
