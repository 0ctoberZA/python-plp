my_list = [10, 20, 30, 40]

# insert 15 in second index.
my_list.insert(1, 15)

# extend list with another list [50, 60, 70]
my_other_list = [50, 60, 70]
my_list.extend(my_other_list)

# remove last element
my_list.remove(70)

# sort list
my_list.sort()

# find an index of value 30
index = my_list.index(30)
print(index)
