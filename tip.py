def main():
     dollars = dollars_to_float(int(input("how much was the meal: ")))
     percent = percent_to_float(int(input("what percentage do you want to leave: ")))
     tip = dollars * percent
     print(f"leave ${tip:.2f}")


def dollars_to_float(D):

   return float(D)

def percent_to_float(p):

      return float(p/100)

if __name__ == "__main__":
     main() 