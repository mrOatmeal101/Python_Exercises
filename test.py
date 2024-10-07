# # Section 18 Conditional Logic
# print('hello')

# age = 19
# guests = 0
# isBirthday = False

# # can type age in ipython and it will output 19. 
# if age > 18:
#     print('you can come in')
#     guests += 1
#     if isBirthday:
#         print('happy birthday here is a free drink')
# elif age == 18:
#     print('you can come in but no drinking')
# else:
#     print('you cannot come in')

# # Section 19 Ternary Operators
# color = 'teal'
# print('good choice') if color == 'teal' else print('meh')

# # do if true if condition else do if false

# # Section 20 Boolean Operations
# # Python: and, or, not
# True and False # False
# True and True # True
# True or False # True
# False or True # True
# False or False # False

# not False # True
# not True # False

# x = 102
# x == 103 or x > 100 # False or True --> so True

# # Ticket Example 
# age = 69
# if age < 10 or age >= 65: 
#     print('your ticket is $5')
# else:
#     print('your tickect is $10')

# not age == 69 # False // a way to look at this: not (age == 40) so it is true then it is false.

# # Section 21 Truthiness and Falsiness
# # Truthiness
# # In Python, these things are falsy:
#     # 0, 0.0, "", None, False
#     # [] (empty list), {} (empty dictionary), set() (empty set)
# # In Python, these things are truthy:
#     # Any non-empty string, non-empty list/dict/set, non-0 number
#     # True

# # Section 22 While Loops
# num = 0

# while num <= 100:
#     if num == 50:# how to break the loop 
#         break
#     print(num)
#     num = num + 10 # or num += 10 but cannot use num++ or num--

# print('all done')

#build a loop that runs an indefinite number of times.
#built in function called input - useful way to get input from the command line or terminal.
# exampleguess = input('enter your guess ') # you enter your input on the terminal and then when you type guess it will be what you inputed. 

#another example of how to use input function.
# target = 37
# guess = None
# #this will allow you to keep putting in inputs until you guess the right number which is 37
# while guess != target:
#     guess = input('please enter a guess... ')
#     if guess == 'q' or guess == 'quit': #this allows you to break the loop before you guess the right number
#         break
#     guess = int(guess)

# print("all done")

# Section 23 For Loops
#for(let i = 10; i < 50; i++){} there is no way to do this type of loop in python.
#but there is one a for of loop in python but it just uses for and in but it is not a for in loop
# this will print out all of the strings on their own line
# colors = ['red', 'green', 'blue', 'yellow']
# for color in colors:
#     print(color)

# this will print out all of the strings on their own line.
# for char in "abcdefghijklmnopqrstuvwxyz":
#     print(char)

# this will print hello 5 times. There is a different way to do this by using the range function. 
# for num in 'abcde':
#     print('hello')

# for nums in [1,2,3,4,5]:
#     print(nums)

# # range function
# for n in range(10):
#     print(n)

# Section 24 Ranges
# range has parameters: range(stop) or range(start, stop[, step]) step is an interval
# range obj will always take the same amount of memeroy as it only stores the start, stop and step.
# for num in range(9):
#     print num

# Examples of how to make different list using the range function. 
# start at 0 and increase by 1 and stop at, but do not include 10. 
# print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # start at 5 and increase the number by 1 and stop at, but do not include 10.
# print(list(range(5, 10))) #[5, 6, 7, 8, 9]

# # start at -10 and increase by 1 and stop at, but do not include 0.
# print(list(range(-10, 0))) #[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# # start at 1, increase the number by 2 and stop at but do not include 10.
# print(list(range(1, 10, 2))) #[1, 3, 5, 7, 9]

# # start at 2, increase the number by 2 and stop at but do not include 12.
# print(list(range(2, 12, 2))) #[2, 4, 6, 8, 10]

# # start at 10, decrease by 4 and stop at but do not include 0. 
# print(list(range(10, 0, -4))) #[10, 6, 2] 

# Section 25 Python Functions
# # 1st simple function in python
# def greet(person): # def is the keyword for function in Python so it is def name_of_function(input)
#     return f"hello there, {person}" 
# # in ipython you then need to call on the function by typing in greet('name_of_person')
# # output will be: 'hello there, cody'
# # functions that don't explicitly Return return None 
#     # if you did print(f'hello there, {person}') instead of return and then stored it in a variable
#     # if you checked the type of that variable it would come back as nonetype. 

# def divide(a,b): # can have as many inputs as you want just like javascript and order does matter
#     if type(a) is int and type(b) is int:
#         return a/b
#     return 'must use an integers' # dont need to use else here b/c like JS, return ends the function. 
# # In [12]: divide(4,2)
# # Out[12]: 2.0
# # In [14]: divide('a',2)
# # Out[14]: 'must use an integers'

# Section 26 Function Arguments
# 

# Section 27 Comments and docstrings
# 

# Section 28 Python Syntax Exercise

