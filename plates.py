
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (is_correct_length(s) and
            starts_with_two_letters(s) and
            numbers_at_end(s) and
            no_invalid_characters(s))


def is_correct_length(s):
    return 2 <= len(s) <= 6


def starts_with_two_letters(s):
    return s[:2].isalpha()


def numbers_at_end(s):
    if any(char.isdigit() for char in s):
        first_digit_index = next(i for i, char in enumerate(s) if char.isdigit())
        if first_digit_index < 2 or s[first_digit_index] == '0':

          return False
        return s[first_digit_index:].isdigit()
    return True


def no_invalid_characters(s):
    return s.isalnum()


main()
