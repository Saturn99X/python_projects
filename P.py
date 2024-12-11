try:
    while True:
        user_input = input("Enter something (Ctrl + D to exit): ")
        print(f"You entered: {user_input}")
except EOFError:
    print("\nEOFError detected. Exiting the program.")