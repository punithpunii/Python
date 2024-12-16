items=[23,45,12,38,10,3,56]

def sum_of_list(items):
    total = 0
    for item in items:
        total += item
    return total

print("sum all the items in a list:",sum_of_list(items))