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
def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.
    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)
    Return results of conversion, if any.
    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".
    For example: convert_temp("c", "f", 0)  =>  32.0 / convert_temp("f", "c", 212) => 100.0
    """
    # YOUR CODE HERE
    


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")
