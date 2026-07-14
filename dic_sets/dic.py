# =====================================================================
# Topic: Dictionaries
# Description: Practice with Python dictionaries, which are collections
#              of key-value pairs that are ordered (since Python 3.7) and mutable.
# =====================================================================

# --- 1. Dictionary Initialization ---
# Creating a dictionary with keys of different types and values as lists/integers
dic = {
    "Anas": 100,
    "saad": 101,
    "list": [100, 101],
    1: 2
}

# --- 2. Accessing Dictionary Elements ---
# Accessing values using keys (direct lookup)
print(dic["Anas"])
print(dic["list"])

# Accessing keys, values, and item pairs
print(f"values: {dic.values()}")
print(f"Keys: {dic.keys()}")
print(f"Items: {dic.items()}")

# --- 3. Modifying and Querying the Dictionary ---
# update() adds or modifies key-value pairs
dic.update({"1": 3})
print(dic)
dic.update({"talha": 99})
print(dic)

# get() safely retrieves a value for a key without raising an error if the key doesn't exist
print(dic.get("1"))

# pop() removes a key and returns its value; returns default (None) if the key is missing
removed_value = dic.pop("Anas", None)
print(f"Removed value: {removed_value}")

# --- 4. Advanced Dictionary Methods ---
# copy() creates a shallow copy of the dictionary
dic_copy = dic.copy()
print(f"Copied dictionary: {dic_copy}")

# clear() removes all elements, making the dictionary empty
dic.clear()
print(f"Dictionary after clear: {dic}")

# setdefault() returns the value of a key if it is in the dictionary; 
# if not, it inserts the key with a specified value (42 in this case)
default_value = dic.setdefault("new_key", 42)
print(f"Default value set for 'new_key': {default_value}")
print(dic)