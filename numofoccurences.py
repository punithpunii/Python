import array

arr=array.array('i',[22,4,5,6,5,3,5,22])
ele=5
count=0
for num in arr:
    if num==ele:
        count+=1

print("the element",ele,"is present",count)