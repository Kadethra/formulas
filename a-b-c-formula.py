import math

def get_zero_point(a: int | float, b: int | float, c: int | float):
    usq = b ** 2 - 4 * a * c
    if usq < 0:
        return "No zero point"

    sqr = math.sqrt(usq) # Alternative without math: usq ** 0.5

    a2 = 2 * a

    x1 = (-b + sqr) / a2
    x2 = (-b - sqr) / a2

    return x1, x2

if __name__ == "__main__":
    from utils import get_number

    a = get_number("a")
    b = get_number("b")
    c = get_number("c")

    out = get_zero_point(a, b, c)
    print(*out, sep="\n")
