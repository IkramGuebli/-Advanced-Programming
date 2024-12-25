def print_characters_with_stars(input_string):
    for char in input_string:
        print(char)
        print("*")

if __name__ == "__main__":
    user_input = input("Please type in a string: ")
    print_characters_with_stars(user_input)
