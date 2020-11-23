# reverse an array challenge


# array reverse code challenge

import numpy as np

    # big daddy string to get things done
def string_to_array_to_reversed_array():
        # function for handling user input
    def user_input_function(user_input): # user_input to take in the input when called, non-keyword parameter string_arg to take in the string from user_input as a list
        user_input = list(user_input.replace(" ", "")) # user_input takes in param string as a list, while within the list user_input.replace trims any white space from user input
        return np.array(user_input, order = 'C') # return user_input list as array in contiguous order

        # function for reversing the array
    def reverse_array(array_arg): # array_arg to take in the np.array values.
        return np.flipud(array_arg) # FLIPS THE ARRAY, DOESN'T REVERSE IT. YOU SEE THE FLIPUD part right?. NOTHING WAS SAID ABOUT FLIPPING.

    # decided to just use a variable here to store the results for printing
    result = reverse_array(user_input_function(input("Please type in a single word as a string: ")))
    print(result) # RESULTS ARE IN!

# call string_to_array_to_reversed_array function and make shit happen
string_to_array_to_reversed_array()