# alternate way to reverse the array (actually it's a list) without numpy
# credit also goes to xable0162 for helping me figure out things like changing array_list.append(array_list(i)) to append(array_list[i])
# thanks man, we pulled it off

# function for reversing
def reverse_list_array(array_list): # array_list param to keep from initializing variable
    for i in range(len(array_list)-1): # loop through the range of array_list's length (-1 because len starts at 1)
        array_list.append(array_list[i]) # append array_list with i's corresponding value (appends it to the end of array_list so nbd)
        array_list.pop(i) # pops (removes) item at the index location of i, preventing duplicates
    return array_list # return list

this_is_a_list_array = ["H", "e", "l", "l", "o", "!"]

print(reverse_list_array(this_is_a_list_array))
