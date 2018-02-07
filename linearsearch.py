import sys

a=raw_input("Enter search")

print a
print type(a)
Found = 1
Element = ['4',6,7,8,9]

for i in Element:
    if i==a:
     Found = 0
     print "Found"

