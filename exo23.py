def main():
    while True:
        try:
            # Ask the user for a positive integer N
            N = int(input("Enter a positive integer: "))
            if N <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    print(f"Input: {N}")

    # Print numbers from -N to N (excluding 0)
    for i in range(-N, N + 1):
        if i != 0:
            print(i)

if __name__ == "__main__":
    main()
