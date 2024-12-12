dhyear=int(input("Enter dog age in human yrs:"))
if dhyear<0:
    print("Invalid age")
elif dhyear<=2:
    ddyear=dhyear*10.5
else:
    dhyear-=2
    ddyear=10.5*2+dhyear*4
print(f"dog age is {int(ddyear)} dog yrs")

