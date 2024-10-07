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
def in_range(nums, lowest, highest):
    """Print numbers inside range.
    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print
    For example:
      in_range([10, 20, 30, 40], 15, 30)
    should print: 20 fits 30 fits"""

    # YOUR CODE HERE


in_range([10, 20, 30, 40, 50], 15, 30)   