my_tuple = (1, 2, 2, 3, 4, 4, 5)
repeated_items = []
checked_items = []


for item in my_tuple:
    if item not in checked_items:
        count = 0
        for i in range(len(my_tuple)):
            if my_tuple[i] == item:
                count += 1
                if count > 1:
                    repeated_items.append(item)
            checked_items.append(item)

print(repeated_items)