import cmath


def quadratic(a, b, c):
    discriminant = cmath.sqrt(b**2.0 - 4.0 * a * c)
    x1 = (-b + discriminant) / (2.0 * a)
    x2 = (-b - discriminant) / (2.0 * a)
    return x1, x2
