list1=[12,67,76,90,89,75,34]
list2=[23,45,75,38,12,34,56]

def append_list(list1, list2):
    for item in list2:
        list1.append(item)
    return list1

print(append_list(list1,list2))