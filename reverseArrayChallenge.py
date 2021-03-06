# reverse an array challenge

# gotta have numpy
import numpy as np

# big daddy string to get things done
def string_to_array_to_reversed_array():
    
    # for handling user input
    def user_input_function(user_input): # user_input to take in the input when called
        user_input = list(user_input.replace(" ", "")) # user_input is reassigned it's input string as a list, while user_input.replace trims any white space out
        return np.array(user_input, order = 'C') # return user_input list as an array in contiguous order to array_arg parameter in reverse_array function

    # for reversing the array
    def reverse_array(array_arg): # array_arg takes in the return from user_input_function
        return np.flipud(array_arg) # FLIPS THE ARRAY, DOESN'T REVERSE IT. YOU SEE THE .flipud part right?. NOTHING WAS SAID ABOUT FLIPPING. ONLY REVERSING.

    # x assigned to take in final return value and store it for printing
    x = reverse_array(user_input_function(input("Please type in a single word as a string: "))) # get user input
    return x # RESULTS ARE IN!

# call "main" function and make shit happen, store in reversed_array for printing.
reversed_array = string_to_array_to_reversed_array()
print(reversed_array)
