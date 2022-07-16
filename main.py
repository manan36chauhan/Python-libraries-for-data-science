a = int(input("Enter the value for factorial number:"))

for i in range(1,a+1):
    for j in range(i,i+1):
        for k in range(i,a):
            print(i,end=" ")
        print()