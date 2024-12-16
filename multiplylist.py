items=[23,45,12,38,10,3,56]

def multiply_of_list(items):
    result = 1
    for item in items:
        result *= item
    return result

print("product all the items in a list:",multiply_of_list(items))