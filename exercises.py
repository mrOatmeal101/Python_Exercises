# Step One: Working in Python Files
# For all the syntax challenges, do your work in script files (Python files normally end with .py). 
# We’ve provided a starter file for each of these with the problem statement and simple print-style tests already.
# count_up.py
# in_range.py
# sum.py
# any7.py
# convert.py
# If you need a reminder of how to convert between Farenheit and Celsius, feel free to Google this
# You can run a Python script in one of two ways:
# When you’re already in IPython, you can run a script with %run myscript.py. 
# This runs your script and leaves you in IPython, where you can examine variables, run functions, etc, from your script. 
# This is often the best way to try things out.
# From the shell, you can run your script as python3 myscript.py
# Step Two: Starting On Your Own

# count_up.py
# def count_up(start, stop):
#     """Print all numbers from start up to and including stop.
#     For example:
#         count_up(5, 7)
#    should print: 5 6 7 """
#     # YOUR CODE HERE
#     return list(range(start, stop+1, 1))

# print(count_up(5, 7))

# in_range.py
# def in_range(nums, lowest, highest):
#     """Print numbers inside range.
#     - nums: list of numbers
#     - lowest: lowest number to print
#     - highest: highest number to print
#     For example:
#       in_range([10, 20, 30, 40], 15, 30)
#     should print: 20 fits 30 fits"""

#     # YOUR CODE HERE
#     for num in nums:
#         first_num = nums[0]
#         last_num = nums[-1]
#         if first_num < lowest and last_num > highest:
#             return f"{lowest} fits {highest} fits"
        
# print(in_range([10, 20, 30, 40, 50], 15, 30))

# sum.py
# def sum_nums(nums):
#     """Given list of numbers, return sum of those numbers.
#     For example:
#     sum_nums([1, 2, 3, 4])
#     Should return (not print): 10
#     """  
#     # Python has a built-in function `sum()` for this, but we don't
#     # want you to use it. Please write this by hand.

#     # YOUR CODE HERE
#     total = 0 # setting variable named total to zero to store the values of total + num as the for in loop runs 
#     for num in nums: # for variable named num loop over the list nums and store each individual element in num
#       total += num # setting the variable total = total + num 
#     return total

# print("sum_nums returned", sum_nums([1, 2, 3, 4]))

# any7.py
# def any7(nums):
#     """Are any of these numbers a 7? (True/False)"""

#     # YOUR CODE HERE
#     for num in nums: # creating a for in loop: making variable num which is storing the individual elements in the list nums.
#       if 7 in nums: # using if statement to determine if the integer 7, then using in keyword, to check an see if the integer 7 is in the list nums
#         return True # return true if it is in the list 
#       else:
#         return False # return false if it is not in the list

# print("should be true", any7([1, 2, 7, 4, 5]))
# print("should be false", any7([1, 2, 4, 5]))

# convert.py
# def convert_temp(unit_in, unit_out, temp):
#     """Convert farenheit <-> celsius and return results.
#     - unit_in: either "f" or "c" 
#     - unit_out: either "f" or "c"
#     - temp: temperature (in f or c, depending on unit_in)
#     Return results of conversion, if any.
#     If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".
#     For example: convert_temp("c", "f", 0)  =>  32.0 / convert_temp("f", "c", 212) => 100.0
#     """
#     # YOUR CODE HERE
#     if unit_in == 'c' and unit_out == 'f':
#         cel_to_far = temp * (9/5) + 32
#         return f'new temp is {cel_to_far}'
#     if unit_in == "f" and unit_out == "c":
#         far_to_cel = (temp - 32) * (5/9)
#         return f'new temp is {far_to_cel}'
#     if unit_in == unit_out:
#         return f'the temp is still {temp}'
#     else:
#         return 'invalid unit'

# print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
# print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
# print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
# print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
# print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

# Step Two: Starting On Your Own
# Do this work in a new file, words.py.
# 1. For a list of words, print out each word on a separate line, but in all uppercase. 
# How can you change a word to uppercase? Ask Python for help on what you can do with strings!
# 2. Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)
# def print_upper_words(words_in):
#     for words in words_in:
#         print (words.upper())

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

# 3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
# 4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that 
# start with one of those letters. For example: this should print "HELLO", "HEY", "YO", and "YES"
# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

# def print_upper_words(words_in): # function called print_upper_words(input variable with the name words_in)
#     for words in words_in: # using for in loop to loop over elements in the input list 
#         for letters in words: # nested for in loop to loop over the individual letters in the input elements
#             if words[0] == 'e' or words[0] == 'y' or words[0] == 'E' or words[0] == 'Y': # if statement to see if the index value of 0 is equal to the string 'e' and if so exacute the following
#                 print(words.upper()) # print the whole input element from word
#                 break      # added break or it will loop over 12 times for the 1st input and will print the element 3 times. 

# print_upper_words(["hello", "hey", "exercise", "goodbye", "yo", "Yes"])
# print_upper_words(["hello", "Eggcellent", "exercise", "goodbye", "yo", "examples"])



