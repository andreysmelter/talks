"""
This module contains routines for finding 
roots of quadratic equations.
"""

import cmath


def quadratic(a, b, c):
    """Solve quadratic equation.
    
    :param float a: a coefficient of a quadratic equation.
    :param float b: b coefficient of a quadratic equation.
    :param float c: c coefficient of a quadratic equation.
    :return: quadratic equation roots.
    :rtype: :py:class:`tuple`
    """
    discriminant = cmath.sqrt(b**2.0 - 4.0 * a * c)
    x1 = (-b + discriminant) / (2.0 * a)
    x2 = (-b - discriminant) / (2.0 * a)
    return x1, x2
