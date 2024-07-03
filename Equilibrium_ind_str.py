def equilibrium_index(my_str):
    my_list = my_str.split(',')   # => string to list
    my_list = [int(n) for n in my_list]  # => converting the list of strings to a list of ints

    for x in range(0,len(my_list)):
        if sum(my_list[:x]) == sum(my_list[x+1:]):
            return x

    return False

nums = '2, 3, 10, 5'
print(equilibrium_index(nums))  # => 2

nums = '3, 3, 10, 5'
print(equilibrium_index(nums))  # => False
