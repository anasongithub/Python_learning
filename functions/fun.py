# =====================================================================
# Topic: Functions and Recursion
# Description: Practice with function definitions, default parameters,
#              list/string manipulation, and recursive functions.
# =====================================================================

# --- 1. Basic Functions and Default Parameters (Commented Reference) ---
# Practice with basic function definition, return values, and default arguments.
#
# def fun(hello, world="world"):  # FUNCTION DEFINITION with a default argument
#     print(hello, world)
#     return "PRINT DONE"
#
# fun("hello")  # function call with one parameter (uses default for 'world')
# fun("hello2", "world2")  # function call with both parameters provided
# # fun()  # Gives an error because 'hello' has no default value
# a = fun("hello3")
# print(a)


# --- 2. Custom Logic Functions (Active) ---
# Predefined list of names (Note: naming a variable 'list' overrides the built-in list type)
list = ["anas", "saad", "talha", "areeba", "adeeba", "yumna"]

# A function to filter out a target word and strip specific characters from other items
def stripWord(list, word):
    n = []
    for item in list:
        if not (item == word):
            n.append(item.strip(word))
    return n

# Call and print the result of the stripWord function
print(stripWord(list, "ee"))


# --- 3. Recursion Practice ---

# A. Recursive Number Printing (Active Function, Commented Call)
def printN(n):
    if (n >= 0):
        print(n)
        return printN(n - 1)
    else:
        return 0

# printN(6)


# B. Recursive Factorial (Commented Reference)
# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# n = factorial(5)
# m = factorial(6)
# print(f"factorial of 5 is: {n} and factorial of 6 is {m}")


# C. Recursive Pattern Generation (Commented Reference)
# def pat(n):
#     if (n <= 0):
#         return
#     else:
#         print("*" * n)
#         pat(n - 1)
#
# n = int(input("Enter Number of Rows to print pattern: "))