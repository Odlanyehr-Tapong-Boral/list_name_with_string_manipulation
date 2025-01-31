names = []

while True:
    input_name = input("Do you want to add a name to the list?: ")
    if input_name == "yes" or input_name == "Yes" or input_name == "YES" or input_name == "Y" or input_name == "y":
       add = input("Enter name here: ")
       names.append(add)
       print(f"Added {add} to list")
    elif input_name == "no" or input_name == "No" or input_name == "NO" or input_name == "N" or input_name == "n":
       print("No names added.")
    else:
       print("invalid input, enter yes or no")

    uppercase_names = [name.upper() for name in names]
    sorted_names = sorted(names)
    reverse_sorted_names = sorted(names, reverse=True)
    vowels = "aeiouAEIOU"
    names_without_vowels = [''.join([char for char in name if char not in vowels]) for name in names]
    
    print("Original Names:", names)
    print("Uppercase Names:", uppercase_names)
    print("Sorted Names:", sorted_names)
    print("Reverse Sorted Names:", reverse_sorted_names)
    print("Names Without Vowels:", names_without_vowels)

    delete = input("Do you want to delete a name from the list? ")
    if delete == 'yes' or delete == 'Yes' or delete == 'YES' or  delete == 'Y' or delete == 'y':
        name_delete = input("Enter the name you want to delete: ")
        if name_delete in names:
            names.remove(name_delete)
            print(f"Deleted: {name_delete}")
        else:
            print(f"Name '{name_delete}' not found in the list.")
    elif delete == 'no' or delete == 'No'or delete == 'NO' or delete == 'N' or delete == 'n':
        print("No names deleted.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        
    uppercase_names = [name.upper() for name in names]
    sorted_names = sorted(names)
    reverse_sorted_names = sorted(names, reverse=True)
    vowels = "aeiouAEIOU"
    names_without_vowels = [''.join([char for char in name if char not in vowels]) for name in names]
    
    print("Original Names:", names)
    print("Uppercase Names:", uppercase_names)
    print("Sorted Names:", sorted_names)
    print("Reverse Sorted Names:", reverse_sorted_names)
    print("Names Without Vowels:", names_without_vowels) 

    continue_list = input("Do you want to continue? ")
    if continue_list == 'yes' or continue_list == 'Yes' or continue_list == 'YES' or continue_list == 'Y' or continue_list == 'y':
        continue
    elif continue_list == 'no' or continue_list == 'No'or continue_list == 'NO' or continue_list == 'N' or continue_list == 'n':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    break

print()
final = "Final names on the list"
(print(final.center (50, "=")))
print("Original Names:", names)
print("Uppercase Names:", uppercase_names)
print("Sorted Names:", sorted_names)
print("Reverse Sorted Names:", reverse_sorted_names)
print("Names Without Vowels:", names_without_vowels) 