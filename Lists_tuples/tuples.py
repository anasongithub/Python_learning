#immutable dataype
t = ('Hello', 1, 2.2, False)
print(t)
print(type(t))
n = (3, 1, 2 ,5,2,6,3,34,6,36,)
print(n.count(2))
# Tuple methods examples

# 1. index() - Returns the index of the first occurrence of a value
index_of_2 = n.index(2)
print(f"The index of the first occurrence of 2 is: {index_of_2}")

# 2. count() - Returns the number of occurrences of a value
count_of_2 = n.count(2)
print(f"The count of 2 in the tuple is: {count_of_2}")

# 3. len() - Returns the number of elements in the tuple
length_of_t = len(t)
print(f"The length of the tuple t is: {length_of_t}")

# 4. max() - Returns the largest element in the tuple
max_value_n = max(n)
print(f"The maximum value in tuple n is: {max_value_n}")

# 5. min() - Returns the smallest element in the tuple
min_value_n = min(n)
print(f"The minimum value in tuple n is: {min_value_n}")