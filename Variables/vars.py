# =====================================================================
# Topic: Variables, Data Types, Type Casting, and Input Handling
# Description: Practice with declaring variables, identifying their
#              types, converting types (casting), and reading input.
# =====================================================================

# --- 1. Variable Declarations and Basic Data Types ---
# Assigning values of different data types to variables
a = 10                     # Integer (int)
b = True                   # Boolean (bool)
c = 10.1                   # Floating-point number (float)
d = None                   # NoneType (represents the absence of a value)
e = "variables are easy?"  # String (str) - Note: Strings in Python are immutable
f = '2'                    # String (str) representing a digit

# Print the types of all the variables declared above
print(type(a), type(b), type(c), type(d), type(e), type(f))

# --- 2. Type Casting (Type Conversion) ---
# Converting the string '2' to an integer using the int() constructor
g = int(f)
print(type(g))

# --- 3. User Input and Dynamic Casting ---
# Using input() to get user input from the console (returns a string)
h = input("Enter a Number: ")
print("H = ", type(h))

# Casting the input string to an integer on the fly for verification
print("H as an int: ", type(int(h)), " : ", int(h))