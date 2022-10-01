import math
from utils import get_number

def Pythagoras(a: float = None, b: float = None, c: float = None) -> float:
    sol = None
    if a and b:
        sol = math.sqrt(pow(a, 2) + pow(b, 2))
    elif (a or b) and c:
        sol = math.sqrt(pow(c, 2) - pow(a or b, 2))
    return sol

def get_vals():
    print("Please input the variables you know.")
    vals = {}
    mind = 2
    while True:
        x = input(f"Which variable? [a, b, c]: ")
        possible = ["a", "b", "c"]
        if x in possible:
            vals.update({x: get_number(x)})
            mind -= 1
        else:
            print("The input have to be numeric")
        
        if not mind:
            return vals


if __name__ == "__main__":
    vals = get_vals()
    res = Pythagoras(**vals)
    print(round(res, 2))
