# my alternate, no numpy solution for list reversing

# reverse function start
def reverse_list_array(a_list, **kwargs):
    kwargs = {"TheList":a_list[::-1]} # use dictionary to store a_list values
    if len(a_list) != 0: # if a_list length isn't zero, clear the list.
        a_list.clear()
    for val in kwargs.values(): # iterate through kwargs values
        a_list.append(val) # append val to a_list while doing so
    return a_list

this_is_a_list_array = ["H", "e", "l", "l", "o", "!"]

print(reverse_list_array(this_is_a_list_array))
