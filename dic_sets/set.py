# =====================================================================
# Topic: Sets
# Description: Practice with Python sets, which are unordered
#              collections of unique elements.
# =====================================================================

# --- 1. Set Initialization vs. Dictionary Initialization ---
# {} creates an empty dictionary, not an empty set
e = {}
print(f"Empty curly braces create type: {type(e)}")

# To create an empty set, you must use the set() constructor
s = set()
print(f"set: {s}, type: {type(s)}")

# --- 2. Set Uniqueness and Length ---
# Sets automatically eliminate duplicate elements
s1 = {1, 2, 2, 3, 4, 5, 5, 5}
print(f"Duplicates removed: {s1}")
print(f"Length of s1: {len(s1)}")

# Sets can contain elements of different data types (as long as they are hashable/immutable)
s2 = {1, 2, 3, 4, "anas"}
print(s2)