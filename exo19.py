def main():
    unique_words = set() 
    total_words = 0  

    while True:
        word = input("Enter a word: ").strip()  

        if word.lower() in unique_words: 
            print(f"You typed in {len(unique_words)} unique words.")
            print("Unique words:", sorted(unique_words))  
            break
        else:
            unique_words.add(word.lower()) 
            total_words += 1 

if __name__ == "__main__":
    main()
