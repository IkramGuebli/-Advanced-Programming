numbers = [1, 2, 3, 4, 5]

while True:
    try:
        index = int(input("Entrez un index (-1 pour quitter) : "))
        if index == -1:
            break
        if index < 0 or index >= len(numbers):
            print("Index invalide. Essayez encore.")
            continue
        
        new_value = input("Entrez une nouvelle valeur : ")
       
        try:
            new_value = int(new_value)
        except ValueError:
            print("Valeur invalide. Vous devez entrer un nombre entier.")
            continue

        numbers[index] = new_value
        print(numbers)
        
    except ValueError:
        print("Entrée invalide. Vous devez entrer un nombre pour l'index.")
