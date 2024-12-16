list1=[12,67,76,90,89,75,34]
list2=[23,45,75,38,12,34,56]

def find_common_items(list1, list2):
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in common:
                common.append(item1)
    return common
print("the common items are",find_common_items(list1, list2))