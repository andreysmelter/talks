"""
This module contains routines for finding 
roots of quadratic equations.
"""

import cmath


def quadratic(a, b, c):
    """Solve quadratic equation.

    For example:
    >>> x1, x2 = quadratic(a=0, b=-8, c=-24)
    """
    discriminant = cmath.sqrt(b**2.0 - 4.0 * a * c)
    x1 = (-b + discriminant) / (2.0 * a)
    x2 = (-b - discriminant) / (2.0 * a)
    return x1, x2


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
