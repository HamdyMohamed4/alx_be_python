def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty shopping list
    
    while True:
        display_menu()  # Display the menu
        
        try:
            choice = int(input("Enter your choice: "))  # Convert input to integer

            if choice == 1:
                # Prompt for and add an item
                item = input("Enter the item you want to add: ")
                shopping_list.append(item)  # Add item to the shopping list
                print(f"'{item}' has been added to your shopping list.")
                
            elif choice == 2:
                # Prompt for and remove an item
                item = input("Enter the item you want to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)  # Remove item from the shopping list
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' not found in your shopping list.")
                    
            elif choice == 3:
                # Display the shopping list
                if shopping_list:
                    print("Current Shopping List:")
                    for i, item in enumerate(shopping_list, start=1):
                        print(f"{i}. {item}")
                else:
                    print("Your shopping list is empty.")
                    
            elif choice == 4:
                print("Goodbye!")  # Exit message
                break  # Exit the loop
                
            else:
                print("Invalid choice. Please select a number between 1 and 4.")  # Handle invalid input

        except ValueError:
            print("Invalid input. Please enter a numeric value.")  # Handle non-integer input

if __name__ == "__main__":
    main()  # Run the main function


