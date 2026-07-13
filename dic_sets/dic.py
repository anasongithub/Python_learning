dic = {
    "Anas": 100,
    "saad": 101,
    "list": [100, 101],
    1: 2
}
print(dic["Anas"])
print(dic["list"])
print(f"values: {dic.values()}")
print(f"Keys: {dic.keys()}")
print(f"Items: {dic.items()}")
dic.update({"1": 3})
print(dic)
dic.update({"talha": 99})
print(dic)
print(dic.get("1"))
# Using the pop method to remove a key and return its value
removed_value = dic.pop("Anas", None)
print(f"Removed value: {removed_value}")

# Using the copy method to create a shallow copy of the dictionary
dic_copy = dic.copy()
print(f"Copied dictionary: {dic_copy}")

# Using the clear method to remove all items from the dictionary
dic.clear()
print(f"Dictionary after clear: {dic}")

# Using the setdefault method to set a default value for a key
default_value = dic.setdefault("new_key", 42)
print(f"Default value set for 'new_key': {default_value}")
print(dic)