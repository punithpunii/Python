items=[23,45,12,38,10,3,56]

def clone_list(items):
    cloned = []
    for item in items:
        cloned.append(item)
    return cloned

print("the copied list:",clone_list(items))