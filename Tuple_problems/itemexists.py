my_tuple = (1, 2, 3, 4, 5)
element = 3
exists = False
for item in my_tuple:
    if item == element:
        exists = True
        break
print(exists)