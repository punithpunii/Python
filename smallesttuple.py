tuples=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def sort_last_element(tuples):
    sorted_list = []
    while len(tuples) > 0:
        smallest = tuples[0]
        for tup in tuples:
            if tup[-1] < smallest[-1]:
                smallest = tup
        sorted_list.append(smallest)
        tuples.remove(smallest)  
    return sorted_list

print(sort_last_element(tuples))