#mutliplication table of a given number
# number = int(input("enter number: "))
# for i in range (1, 10):
#     print(f"{number} * {i} = {number * i}")

#greet names staring with A
# l = ["anas", "areeba", "saad", "adeeba", "talha", "yumna"]
# for i in l:
#     if(i.startswith("s")):
#         print(f"Greetings {i}")

# prime or not

# number = int(input("Enter number to check for prime: "))
# if number <= 1:
#      print("invalid input (1, 0, or negative)")
# else:
#         i = 2
#         prime = True
#         while(i * i <= number):
#             if(number % i == 0):
#                 print(f"{number} % {i} = 0")
#                 prime = False
#                 break
#             i += 1
#         if(prime):
#             print("PRIME")   
#         else: 
#             print("NOT A PRIME")

#factorial
# number = int(input("Enter a number to check for factorial: "))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *=  i
# print(f"factorial of {number} is {factorial}")

#Print pattern
# n = int(input("enter a number: "))
# for i in range(n):
#     for j in range(n):
#         if(((i != 0) and (i != n - 1))):
#             if((j != 0) and (j != n - 1)):
#                 print("  ", end="")
#             else:
#                 print("* ", end="")
#         else:
#             print("* ", end="")
#     print("\n", end="")

#same pattern with one loop

# for i in range(1, n + 1):
#     if(i == 1 or i == n):
#         print("*"* n, end="")
#     else:
#         print("*", end="")
#         print(" "* (n-2), end="")
#         print("*", end="")
#     print("")

