import math

def f(x):
    return (x / 2) - math.sin(x) + (math.pi / 6) - (math.sqrt(3) / 2)

def dichotomie(f, a, b, epsilon=1e-12):
    while (b - a) / 2 > epsilon:
        middle = (a + b) / 2
        if f(middle) == 0:
            return middle
        elif f(a) * f(middle) < 0:
            b = middle
        else:
            a = middle
    return (a + b) / 2


neg_solution = dichotomie(f, -math.pi/2, 0)

pos_solution = dichotomie(f, 0, math.pi)

print(f"Solution strictement négative: {neg_solution}")
print(f"Solution strictement positive: {pos_solution}")
print("thanks for using")
