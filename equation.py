import re

def get_solutions(polynom):
    if match := re.search(r"^([+-]?\d*)x\*\*([0-9]+)([+-]\d*)x([+-]\d+)$", polynom, re.IGNORECASE):

        a = match.group(1)
        b = match.group(3)
        c = match.group(4)
        
        a = int(a) if a and a != '+' and a != '-' else (1 if a == '' or a == '+' else -1)
        b = int(b) if b else 0
        c = int(c)

        if a == 0:
            print("This is not a second-degree equation.")
            return
        
        D = (b**2) - (4*a*c)

        if D < 0:
            print("The equation has no real solutions.")
        elif D == 0:
            x = -b / (2*a)
            print(f"The double-solution of the equation is {x}")
        else:
            sqrt_D = D**0.5
            x1 = (-b - sqrt_D) / (2*a)
            x2 = (-b + sqrt_D) / (2*a)
            print(f"The equation has two solutions: {x1} and {x2}")
    else:
        print("The polynomial format is incorrect.")

def main():
    polynom = input("Input the equation: ")
    get_solutions(polynom)

if __name__ == "__main__":
    main()

