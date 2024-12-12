num=int(input("Enter the num:"))
a=0
b=1
if num==1:
    print(a)
elif num==2:
    print(b)
else:
    for i in range(3,num+1):
        c=a+b
        a=b
        b=c
    print(c)
