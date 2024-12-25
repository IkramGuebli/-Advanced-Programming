def show_menu():
    print("\nMenu:")
    print("1. Append")
    print("2. Insert")
    print("3. Pop")
    print("4. Remove")
    print("5. Quit")

def append_value(lst):
    try:
        value = int(input("Enter value: "))
        lst.append(value)
        print("Updated List:", lst)
    except ValueError:
        print("Invalid input. Please enter an integer.")

def insert_value(lst):
    try:
        value = int(input("Enter value: "))
        index = int(input("Enter index: "))
        if 0 <= index <= len(lst):
            lst.insert(index, value)
            print("Updated List:", lst)
        else:
            print("Invalid index. Index must be within the list bounds.")
    except ValueError:
        print("Invalid input. Please enter integers for both value and index.")

def pop_value(lst):
    try:
        index = int(input("Enter index to pop: "))
        if 0 <= index < len(lst):
            lst.pop(index)
            print("Updated List:", lst)
        else:
            print("Invalid index. Index out of range.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def remove_value(lst):
    try:
        value = int(input("Enter value to remove: "))
        if value in lst:
            lst.remove(value)
            print("Updated List:", lst)
        else:
            print(f"Value {value} not found in the list.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    numbers = [1, 2, 3, 4, 5]
    print("Initial List:", numbers)

    while True:
        show_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            append_value(numbers)
        elif choice == '2':
            insert_value(numbers)
        elif choice == '3':
            pop_value(numbers)
        elif choice == '4':
            remove_value(numbers)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a valid menu option.")

if __name__ == "__main__":
    main()
