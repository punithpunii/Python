list1=[12,67,76,90,89,75,34]
list2=[23,45,75,38,12,34,56]



def difference_lists(list1, list2):
    diff = []
    for item in list1:
        if item not in list2:
            diff.append(item)
    return diff

print("the new list:",difference_lists(list1,list2))