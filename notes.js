// Section 1 Introduction to Python Handout

// Section 2 Introduction to Back-end
// Introduction to Python
// Python is used for server side coding/or back end development. 
// The Dark Side
    // We’ve seen a lot of client-side stuff: HTML, CSS, & JS. There’s even more stuff to learn!
    // It’s time for us to spend some time on the other, more mysterious side…the server side!
    // There are tons of languages we could use to write server-side code with:
        // Ruby
        // JS (Node)
        // PHP
        // Java
// But we’ll be working with Python! (and eventually Node)

// Section 3 Why Python?
// It’s fast, powerful, and widely used
// “high level”: express concepts at a high level (a little more than JS)
// Super clean syntax!
// Runs on servers (but not in a browser)
// Particularly used for data science, machine learning, making servers, etc
// (This comic is from the days of Python 2; in modern Python, that would be print("Hello, world"), with parentheses.

// The Game Plan
// We’ll start by learning basic Python syntax: variables, loops, functions, etc.
// Then we’ll move on to Object Oriented Programming in Python
// We’ll learn how to create our own servers using Python!
// Then it’s on to Python testing
// We’ll take a detour to learn SQL and see how to connect to a DB using Python
// We’ll cover authentication and deployment as well

// Section 4 MacBook 2020 Users: Documentation for Rosetta (3 pages)  Optional 
// Nothing

// Section 5 Installing Python

// Installing Python
// Head over to https://www.python.org/downloads/
// Test that it works: in a new Terminal window
// $ which python3

// Python Versions
// Python 2
// Latest is 2.7
// What some people still use
// What comes by default on OSX
 
// Python 3
// Latest is 3.7
// Slightly different language & syntax
// What we’ll use at Rithm

// Section 6 Python Docs
// To find out more about the version of python you want to use go to:
// https://docs.python.org/3/
// has documentation on all python versions 

// Section 7 IPython and pip
// Install another Python utility: ipython:
// $ pip3 install ipython

// Interactive Python
// IPython is a program for interactive exploring of Python
// $ ipython
    // Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24)
    // Type 'copyright', 'credits' or 'license' for more information
    // IPython 6.5.0: An enhanced Interactive Python. Type '?' for help.

// In [1]: print("Hello, World!")
    // Hello, World
// (type: Control-D to exit)

// Section 8 Windows - Installing pip3
//how to install pip3 and ipython on linux subsystem/windows.

// Section 9 Neural Art Demo
// how to download and install a package with pip3. 
// first example was to type in the console: pip3 install neuralart
// download from: https://pypi.org/project/neuralart/
// to uninstall type: pip3 unistall neuralart

// Section 10 Declaring Variables
// Python variable name style is like_this (lower-snake-case)
// There is no keyword for declaring variables; ie no let or var
// you redefine variables not redeclare them 
    // Redefining a variable: Means assigning a new value to an existing variable. let y = 5; y = 15;
    // Redeclaring a variable: Means declaring a variable with the same name in the same scope. var x = 10; var x = 20;
// No specific way to make un-re-bindable like const
    // It’s good style to write constants LIKE_THIS - upper case means don't change this and use this as a constant. 
// “Lexical function scoped” - variables are scoped to functions. 
// x = 42 - outside the function
// def my_function():
//     x = 12 - inside a function
//     print(x)   # 12
// print(x)       # 42

// Section 11 Python Numbers
// Numbers
// Very much like JavaScript!
// Separate types for integers (can be any size) or floating-point
// there are int(whole numbers), float(non-whole numbers) and complex numbers in Python (complex(3,32) will output 3,32j)
    // In JS, there are only floating-point numbers
    // Separate type for complex numbers
// +, -, *, / (true division), // (integer division)
// % (modulo: remainder after division)
// Dividing by zero is an error (JS: is Infinity, except 0/0, which is NaN)
// Can use + and * on strings: "cat" + "food" or "yay" * 3
// if you use double divide (//) i.e. integer division it will floor the answer. 10/3 = 3.33333 -> 10//3 = 3 
// int(3.333) = 3 or float(3) = 3.0 to convert numbers to integers or floats.
// round(3.14519,2) will round the number to 2 decimal places which will output 3.14
// some built in methods
    // 4.56.is_integer() will output false 4.00.is_integer() will output true
    // 2323487.21.hex() will give you the hexidecimal representation which is '0x1.1ba0f9ae147aep+21'

// Section 12 Stings
// All alphanumeric text is held in a data structure called a string. In Python, the str class represents a 
// collection of one or more Unicode characters. Learn more about this fundamental concept in this video. 
// Like JS, can use " or ' as delimiters
// Can be multi-line by using triple-quotes: """ or '''
    // ''' <div>
    //  <h1>Hi<h1>
    // </div>
    // will output '\n<div>\n   <h1>Hi<h1>\n</div>\n '
    // so python will know to auto format with the \n 
// Can interpolate expressions with f-strings:
    // stands for formated strings
    // food = "cheese"
    // print(f"I love {food}") - this tells python that {food} should be evaluated and turned into a string
        // this is how you do string template literals in python
    // f"2+2={2+2}"
        // '2+2=4
    // first = 'james'
    // last = "tatum"
    // full = f"mr.{first} - {last}"
        // full // 'mr.james - tatum'
    // \t is tab - print('\t hi') - it will be indented
    // \n new line - print('hi \n hello') - will have hi on one line and hello on the next. 

// Section 13 List
// Lists
// list are similar to arrays in javaScript 
// work almost the same way as arrays in javaScript
// Like JS arrays:
    // ordered
    // can be heterogeneous: [1, "apple", 13.5]
    // In [33]: people = ['john', 'ringo']
    // In [34]: people
    // Out[34]: ['john', 'ringo']

// Section 14 Boolean Comparisons
// Truthiness
// need to use capital T in Python ==> True not true
// In JS, these things are falsy:
    // 0, 0.0, "", undefined, null, NaN, false
// In JS, these things are (perhaps unexpectedly) truthy:
    // [], {}
// In Python, these things are falsy:
    // 0, 0.0, "", None, False (make sure to capitalize the F)
    // [] (empty list), {} (empty dictionary), set() (empty set)
// In Python, these things are truthy:
    // Any non-empty string, non-empty list/dict/set, non-0 number
    // True (make sure to capitalize the T)

// Python does not allow you to compare strings or numbers
    // 1 < 't' will output false 

// Section 15 Equality Operators
// Equality
// JavaScript
// == loose equality
    // 7 == "7"
// === strict equality / do not have the same ref number for storage
    // 7 === "7"  // false
// Objects & arrays only equal when same identity
 
// Python
// == equality (strict about types) 
    // 7 == "7"  # False
    // No loose type equality in python
// Structures with same items are equal
    // [1, 2, 3] == [1, 2, 3] this will output true b/c it doesnt care about reference number
// Use 'is' to check obj identity i.e. you want to check if the list have the same reference number 
    // [1, 2] is [1, 2]  # False
// Use 'is not' for the opposite of 'is'

// Section 16 Indentation
// Remember your English teacher harping on you about properly indenting your paragraphs? Proper indentation is even more important in Python.
// As an indentation-based language, your spacing in Python tells the code interpreter where each function, 
// loop, and every other piece of logic starts and stops. In most other languages, curly braces ({}) tell the code interpreter 
// where each block of logic starts and ends.
// Python is all about removing extraneous code, so it just uses spacing for logic blocks. 
// There's even a famous debate in the Python community over whether tabs or spaces are the better way to format code. 
// Hint: IT'S TABS.

// In many programming languages, you use { and } to show blocks:
// if (age >= 18) {
//   console.log("Please go vote!");
//   registerToVote();
// }

// Programmers also tend to indent this code, but that’s just visually prettiness.
// This would work the same:
// if (age >= 18) {
// console.log("Please go vote!");
// registerToVote();
// }
// (That is so ugly. Please don’t do that.)

// In Python, you don’t use {/} for blocks; the indentation is what matters:
// if age >= 18:
//     print("Please go vote!")
//     register_to_vote() // This will only run if age >= 18

// That’s very different than:
// if age >= 18:
//     print("Please go vote!")
// register_to_vote() // This will run every time. 

// In JS, people often use 2 or 4 spaces for indentation (styles vary)
// In Python, everyone agrees: it should always be 4 spaces

// Section 17 Running Files
// You don't run Python files in the browser. You run them on the server through the command line. Here's how.
// There is no browser for python. 
// How to run a Source File, that you made in VS Code for example, from the terminal. 
// they are .py files for saving purposes. 
// $ python3 name_of_file.py
// Whatever data/text you had stored in your .py file. 
//  $ // after it runs it puts you back in the terminal shell
// runs Python
// loads name_of_file.py
// executes the code
// returns to the terminal when done.

// Running in IPython3
// $ ipython3
// In [1]: %run name_of_file.py
// runs run naem_of_file.py
// stays in IPython, variables are still set
// can also check variables that you declared in ipython

// Section 18 Conditional Logic
// If Statements in Python
// if grade == "A":
//  print("awesome job!")
// elif grade == "F":
//  print("ut oh")
// else:
//  print("don't worry too much")

// (parens around condition aren’t required, unlike JS)

// if age >= 18:
//  if unregistered:
//     print("please register")
//  else:
//     print("keep voting!")
// else:
//  print ("Wait a bit")

// Section 19 Ternary Operators
// Ternary
// JavaScript
// let msg = (age >= 18) ? "go vote!" : "go play!"
// Python
// msg = "go vote!" if (age >= 18) else "go play!"
// (in both, parens are optional but often helpful)

// Section 20 Boolean Operations
// And/Or/Not
// JS: &&, ||, !
// Python: and, or, not
// Just like in JS, these “short circuit”

// Section 21 Truthiness and Falsiness
// Truthiness
// In JS, these things are falsy:
// 0, 0.0, "", undefined, null, NaN, false
// In JS, these things are (perhaps unexpectedly) truthy:
// [], {}
// In Python, these things are falsy:
// 0, 0.0, "", None, False
// [] (empty list), {} (empty dictionary), set() (empty set)
// In Python, these things are truthy:
// Any non-empty string, non-empty list/dict/set, non-0 number
// True

// Section 22 While Loops
// 

// Section 23 For Loops
// 

// Section 24 Ranges
// 

// Section 25 Python Functions
// 

// Section 26 Function Arguments
// 

// Section 27 Comments and docstrings
// 

// Section 28 Python Syntax Exercise
// 
