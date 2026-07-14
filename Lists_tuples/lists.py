# =====================================================================
# Topic: Lists
# Description: Practice with Python lists, which are ordered, mutable,
#              and can store elements of heterogeneous data types.
# =====================================================================

# --- 1. List Initialization and Mutability ---
# Lists are defined using square brackets [] and are mutable (can be changed in-place)
lis = ['hello', 1, 2.2, "anas", False, None]
print(lis)

# Modifying an element at a specific index (demonstrates mutability)
lis[0] = "hello2"
print(lis)

# --- 2. Modifying Lists (Adding and Inserting Elements) ---
# append() adds an element to the end of the list
lis.append("appended")
print(lis)

# insert() inserts an element at a specific index (index 2 in this case)
lis.insert(2, "insertedat2")
print(lis)

# --- 3. Modifying Lists (Removing Elements) ---
# pop() removes and returns the element at the specified index (index 2)
print(lis.pop(2))
print(lis)

# Other list methods for sorting and reversing (commented out for reference)
# lis.sort()
# lis.reverse()

# remove() removes the first occurrence of a specific value (value 1 in this case)
# Note: remove() returns None while modifying the list in-place
print(lis.remove(1))
print(lis)