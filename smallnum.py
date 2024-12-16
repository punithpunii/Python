items=[23,45,12,38,10,3,56]

def smallest_in_list(items):
    smallest = items[0]
    for item in items:
        if item < smallest:
            smallest = item
    return smallest

print("the smallest num is:",smallest_in_list(items))