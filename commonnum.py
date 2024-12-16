list1=[23,45,12,38,10,3,56]
list2=[12,67,76,90,89,75,34]

def have_common_member(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False
print(have_common_member(list1,list2))


