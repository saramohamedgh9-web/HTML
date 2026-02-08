#empty tuple
my_tuple = ()
print(my_tuple)  # Output: ()

#nested tuple
nested_tuple = (1, 2, (3, 4), [8, 9], 5)
print(nested_tuple)  # Output: (1, 2, (3, 4), [8, 9], 5)

#iterating through a tuple
for i in nested_tuple:
    print(i)