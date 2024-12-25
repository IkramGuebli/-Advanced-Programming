numbers = []
shoe_sizes = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

numbers.append(3)

sizes = [8, 9, 10, 11, 12]
for size in sizes:
    shoe_sizes.append(size)

combined_list = numbers + shoe_sizes

print("Numbers List with Duplicates:", numbers)
print("Shoe Sizes List:", shoe_sizes)
print("Combined List:", combined_list)
