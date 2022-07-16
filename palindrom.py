def pal(num):
    x1 = num[::-1]
    if x1 == num:
        print('palindrom')
    else:
        print('not a palindrom')
print(pal('1215'))