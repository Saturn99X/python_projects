
def shorten(input):
    twttr = ""
    for char in input:
        if char in ["a", "e", "i", "o", "u", "A", "E", "I","O", "U"]:
            continue
        else:
            twttr += char
    return twttr

def main():
    user_input = input("input: ")
    output = shorten(user_input)
    print(f"output: {output}")

if __name__ == "__main__":
    main()
