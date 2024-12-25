
def main():
    user_list = []  

    while True:
        try:
            num = int(input("Enter a number (0 to quit): "))
            
            if num == 0:  
                print("Exiting the program.")
                break
            
            user_list.append(num)
            
            print(f"Current List: {user_list}")
            print(f"Sorted List: {sorted(user_list)}")
        
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()

































