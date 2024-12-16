import array
arr=array.array('i',[22,4,5,6,5,3,5,22])

ele=5
new_array = []
for i in range(len(arr)):
        if arr[i] == ele:
                for j in range(len(arr)):
                    if j != i:
                        new_array.append(arr[j])
                break

print(new_array)

