age = int(input("Enter you age: "))

if(age >= 18):
    print("adult")
elif(age <=0):
    print("invalid input")

else: 
    print("Teen")
#elif
names = ["anas", "saad", "talha", "areeba", "adeeba", "yumna"]
parents = ["ammhi", "papa", "mama g", "annhi"]
input = input("Enter Name: ")
if(input.upper() in [name.upper() for name in names]): #list comprehension used to "upper" every name in names
    print(f"{input} is a sibling")
elif(input.upper() in [parent.upper() for parent in parents]):
    print(f"{input} is a parent")
else:
    print("get lost")

#nested if else
if(age >= 18):
    if(age >= 40):
        print("you old, take care of yourself")
    else:
        print("You can do whatever")
else:
    print("you a child")