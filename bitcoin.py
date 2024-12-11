import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price.")

def main():
    if len(sys.argv) < 0:
        sys.exit("missing command line argument")

    try:
        num_bitcoins = float(input("Enter the number of bitcoins: "))
    except ValueError:
        sys.exit("command-line argument must be a number")

    price_per_bitcoin = get_bitcoin_price()
    amount = num_bitcoins * price_per_bitcoin
    print(f"${amount:,.4f}")

if __name__ == "__main__":
    main()
