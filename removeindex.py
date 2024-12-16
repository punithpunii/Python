items=[12,67,76,90,89,75,34]

def remove_specific_indices(items):
    result = []
    for i in range(len(items)):
        if i not in [0, 4, 5]:
            result.append(items[i])
    return result

print("the new list:",remove_specific_indices(items))