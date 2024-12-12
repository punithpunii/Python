num=int(input("Enter the num:"))
x=num
res=0
while x!=0:
    res=res+(x%10)**3
    x=x//10
if num==res:
    print("is Armstrong")
else:
    print("not armstrong")

