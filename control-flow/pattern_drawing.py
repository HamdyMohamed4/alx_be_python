# pattern_drawing.py

# Prompt the user to enter a positive integer for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    
    # Move to the next line after printing each row
    print()
    
    # Increment the row counter
    row += 1
