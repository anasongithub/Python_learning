# =====================================================================
# Topic: Loops (for and while)
# Description: Practice exercises using loops for mathematical tasks,
#              filtering, and console pattern printing.
# Note: All code sections are commented out so they can be run 
#       individually by uncommenting them.
# =====================================================================

# --- 1. Multiplication Table ---
# Generates a multiplication table for a given number using a for loop.
#
# number = int(input("enter number: "))
# for i in range(1, 10):
#     print(f"{number} * {i} = {number * i}")


# --- 2. Greet Names Starting with a Specific Character ---
# Iterates through a list of names and greets those starting with the letter 's'.
#
# l = ["anas", "areeba", "saad", "adeeba", "talha", "yumna"]
# for i in l:
#     if i.startswith("s"):
#         print(f"Greetings {i}")


# --- 3. Prime Number Checker ---
# Verifies whether a number is prime using a while loop with root limit optimization.
#
# number = int(input("Enter number to check for prime: "))
# if number <= 1:
#      print("invalid input (1, 0, or negative)")
# else:
#      i = 2
#      prime = True
#      while (i * i <= number):
#          if (number % i == 0):
#              print(f"{number} % {i} = 0")
#              prime = False
#              break
#          i += 1
#      if prime:
#          print("PRIME")   
#      else: 
#          print("NOT A PRIME")


# --- 4. Factorial Calculation ---
# Computes the factorial of a user-provided integer using a for loop.
#
# number = int(input("Enter a number to check for factorial: "))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print(f"factorial of {number} is {factorial}")


# --- 5. Pattern Printing - Hollow Square (Nested Loops) ---
# Prints a hollow square of size n using nested loops.
#
# n = int(input("enter a number: "))
# for i in range(n):
#     for j in range(n):
#         if (((i != 0) and (i != n - 1))):
#             if ((j != 0) and (j != n - 1)):
#                 print("  ", end="")
#             else:
#                 print("* ", end="")
#         else:
#             print("* ", end="")
#     print("\n", end="")


# --- 6. Pattern Printing - Hollow Square (Single Loop) ---
# Prints the same hollow square pattern of size n optimized using a single loop.
#
# for i in range(1, n + 1):
#     if (i == 1 or i == n):
#         print("*" * n, end="")
#     else:
#         print("*", end="")
#         print(" " * (n - 2), end="")
#         print("*", end="")
#     print("")

