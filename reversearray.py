import array

arr=array.array('i',[2,3,6,87,98,23])

arr1=array.array('i',[0]*len(arr))
j=0
i=len(arr)-1
while j<=len(arr)-1 and i>=0:
    arr1[j]=arr[i]
    j+=1
    i-=1
    

print("reversed array:",arr1)