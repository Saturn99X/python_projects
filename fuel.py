def main():
    user_fuel_input = input("fraction: ")
    fuel_percentage = get_fuel_percentage(user_fuel_input)
    if 0<=fuel_percentage<=1:
         print("E")
    elif 1<fuel_percentage<99:
     print(f"{fuel_percentage}%")
    elif 99<=fuel_percentage<=100:
        print("F")
    else:
        pass

def get_fuel_percentage(remaining_fuel):
    while True:
            try:
                numbers = remaining_fuel.split("/")
                X = int(numbers[0])
                Y = int(numbers[1])
                Z = round(100*(X/Y))
            except:
                  print("bad input")
                  Q = input("fraction: ")
                  remaining_fuel = Q
            if X>Y:
                print("bad input")
                Q = input("fraction: ")
                remaining_fuel = Q
            else:
                break
    return (Z)



main()



