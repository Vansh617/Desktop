# Day 3
Name = "I am Neeraj"
print(id(Name))
print(Name.islower())
print(Name.swapcase())
print(Name.isupper())
print(Name.title())
print(len(Name))
print(Name.isdigit())
print(Name.isalpha())
print(Name.startswith("I"))
print(Name.endswith("j"))

print(Name.strip())  # last and staring space cut kr deta hai
s = "---he--lo-----"
print(s.rstrip("-"))
print(s.lstrip("-"))
print(s.strip("-"))
a = 10
b = 10
print(id(a))
print(id(a + 1))
print(id(b))

# oprators
print(10 + 4)
print("name" + "12")
print(2**4)
print("hello" * 12)
print(7 / 2)
print(7 // 2)
print(3 % 2)
# relational operators
print(5 > 2)
print("hello" < "hi")
print("ant" > "Ant")
# logical operators
# and, or, not

x = 5
y = 10
z = 15
print(x > y > z and y > x and z < y)
print(x * 3 > z or 7 + y < z**3)
print(not (x == y))
print("me" not in "same")
print("me" in "same")
g = "hellllllllllllllllooooooo"
print(g.count("l"))
a = 12
if a > 18:
    print("You can vote")
else:
    print("You can't vote")
import torch
