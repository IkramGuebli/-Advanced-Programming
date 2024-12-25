print("Input:")
nbr = int(input("Number: "))
print("Output:")

if nbr %3 ==0 and nbr%5 ==0: 
    print("FizzBuzz")
elif nbr % 3 == 0:  
    print("Fizz")
elif nbr %5 ==0:
    print("Buzz")
else: 
    print("[No Output]")
