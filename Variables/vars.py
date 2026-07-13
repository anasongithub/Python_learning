a = 10
b = True
c = 10.1
d = None
e = "variables are easy?" # strings are immutable
f = '2'
print(type(a), type(b), type(c), type(d), type(e), type(f))
g = int(f)
print(type(g))
h = input( "Enter a Number: ")
print("H = ", type(h))
print("H as an int: ", type(int(h)), " : ", int(h))