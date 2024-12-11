import random


def main():
    lvl = get_level()
    generate_integer(lvl)

def get_level():
    level = int(input("level: "))
    while level not in [1,2,3]:
        continue
    return level

def generate_integer(level):
    i = 0
    for _ in range(10):
        if level == 1:
            A = random.randint(0,9)
            B = random.randint(0,9)
            C = A+B
            response = int(input(f"{A} + {B}= "))
            while response != C and i<2:
                i += 1
                print("EEE")
                response = int(input(f"{A} + {B}= "))
            if i == 2:
                print(f"{A} + {B} = {C}")
                break
            else:
                continue
        elif level == 2:
            A = random.randint(10,99)
            B = random.randint(10,99)
            C = A+B
            response = int(input(f"{A} + {B}= "))
            while response != C and i<2:
                i += 1
                print("EEE")
                response = int(input(f"{A} + {B}= "))
            if i == 2:
                print(f"{A} + {B} = {C}")
                break
        elif level == 3:
            A = random.randint(100,999)
            B = random.randint(100,999)
            C = A+B
            response = int(input(f"{A} + {B}= "))
            while response != C and i<2:
                i += 1
                print("EEE")
                response = int(input(f"{A} + {B}= "))
            if i == 2:
                print(f"{A} + {B} = {C}")
                break


if __name__ == "__main__":
    main() 