a = int(input("Enter first number:"))
b = int(input("enter second number:"))
n = int(input("Enter number of elements:"))

print(a,b,end=" ")

while n-2:
    c= a+b
    a = b
    b = c
    print(c,end=" ")
    n= n-1