names = []

input_name = input("Do you want to add a name to the list? ")
if input_name == "yes" or input_name == "Yes" or input_name == "YES" or input_name == "Y" or input_name == "y":
    add = input("Enter name here. ")
    names.append(add)
    print(f"Added {add} to list")
elif input_name == "no" or input_name == "No" or input_name == "NO" or input_name == "N" or input_name == "n":
    print("No names added.")
else:
    print("invalid input, enter yes or no")

print(names)

uppercase_names = [name.upper() for name in names]
sorted_names = sorted(names)
reverse_sorted_names = sorted(names, reverse=True)
    
    # Remove vowels from names
vowels = "aeiouAEIOU"
names_without_vowels = [''.join([char for char in name if char not in vowels]) for name in names]
    
print("\nOriginal Names:", names)
print("Uppercase Names:", uppercase_names)
print("Sorted Names:", sorted_names)
print("Reverse Sorted Names:", reverse_sorted_names)
print("Names Without Vowels:", names_without_vowels)