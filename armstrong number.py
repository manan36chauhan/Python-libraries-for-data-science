num = int(input("Enter number to check it is armstrong or not "))
sum =0
temp = num

while temp>0:
    c = temp % 10
    sum += c**3
    temp //= 10
    if num == sum:
       print("armstrong number")
    else:
        print("not armstrong")