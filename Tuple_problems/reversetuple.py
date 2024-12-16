my_tuple = (1, 2, 3, 4)
reversed_tuple = ()
for i in range(len(my_tuple)-1, -1, -1):
    reversed_tuple += (my_tuple[i],)
print(reversed_tuple)