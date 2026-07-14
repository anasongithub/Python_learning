# =====================================================================
# Topic: Conditional Statements (if-elif-else)
# Description: Practice with basic conditions, nesting, list search 
#              (using in operator), and list comprehensions.
# =====================================================================

# --- 1. Basic If-Elif-Else Statement (Age Validation) ---
age = int(input("Enter you age: "))

if (age >= 18):
    print("adult")
elif (age <= 0):
    print("invalid input")
else: 
    print("Teen")

# --- 2. Nested If-Else Statements ---
if (age >= 18):
    if (age >= 40):
        print("you old, take care of yourself")
    else:
        print("You can do whatever")
else:
    print("you a child")

# --- 3. Membership Checking and List Comprehensions ---
# Predefined lists of siblings and parents
names = ["anas", "saad", "talha", "areeba", "adeeba", "yumna"]
parents = ["ammhi", "papa", "mama g", "annhi"]

# Reading a name (Note: assigning to 'input' overrides the built-in input function)
input = input("Enter Name: ")

if (input.upper() in [name.upper() for name in names]):  # list comprehension to upper-case all items
    print(f"{input} is a sibling")
elif (input.upper() in [parent.upper() for parent in parents]):
    print(f"{input} is a parent")
else:
    print("get lost")