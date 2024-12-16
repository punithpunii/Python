items=[23,45,12,38,10,3,56,45,23,12,12,10]


def remove_duplicates(items):
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

print("the new list is :",remove_duplicates(items))