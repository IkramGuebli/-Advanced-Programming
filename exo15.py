string=str(input("please type in a string : ")).lower()


vowels= ['a', 'e', 'o']
for v in vowels:
    if v in string:
        print(f"{v} Found!")
    else:
        print(f"{v} not Found!")