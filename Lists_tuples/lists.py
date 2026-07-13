#lists are mutable
lis = ['hello', 1, 2.2, "anas", False, None]
print(lis)
lis[0] = "hello2"
print(lis)
lis.append("appended")
print(lis)
lis.insert(2, "insertedat2")
print(lis)
print(lis.pop(2))
print(lis)
#lis.sort()
#lis.reverse()
print(lis.remove(1))
print(lis)