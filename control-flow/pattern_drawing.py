# pattern_drawing.py
# A program to draw a square pattern using while and nested for loops

# Prompt user for input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for rows
while row < size:
    # For loop for columns
    for col in range(size):
        print("*", end="")  # Print asterisk without new line
    print()  # Move to the next line after one row
    row += 1
