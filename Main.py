import math
from webbrowser import get

# Variable
# print ("Hello World")
# students_count = 1000
# rating = 4.99
# is_published = True
# course_name = "Python Programming"
# print(Students_count)

# Strings
# course_name = "Python Programming"
# print(len(course_name))
# print(course_name[-1])

# Escape_sequences
# \"
# \'
# \\
# \n
# course = "Python \nProgramming"
# print(course)


# Formated Strings
# first = "Seyed Hassan"
# last = "Mousavi"
# full_name = first + " " + last
# full_name = f"{first} {last} {2 + 2}"
# print(full_name)

# String Methods
# course_name = "Python Programming"
# print (course_name.upper())
# print (course_name.lower())
# print (course_name.title()) #Captalize very start world
# print (course_name.strip()) #Spaces will remove
# print (course_name.find("Pro")) #Find the index
# print (course_name.replace("P", "j")) #Replace characters
# print ("Pro" in course_name)
# print ("swift" not in course_name)

# Numbers
# print (10 + 3)
# print (10 - 3)
# print (10 * 3)
# print (10 / 3)
# print (10 // 3)
# print (10 % 3)
# print (10 ** 3)
# print(round(2.89))
# print(abs(-2.99))
# print(math.ceil(2.2))

# Type conversation
# x = input ("x: ")
# y = int (x) + 1
# print(f"x: {x}, y {y}") # X and Y function

#Comparison Operation
# print (10 > 3)
# print (10 == 3)
# print (10 < 20)
# print (10 == 10)
# print (10 != 10)
# print ("bag" > "apple")
# print ("bag" == "BAG")

#Condional Statements
# temperature = 15
# if temperature > 30:
#     print("Its warm")
#     print("Drink water")
# elif temperature > 20:
#     print("its nice")
# else:
#     print("Its cold")
# print("Done")

#Ternary Operator
# age = 12
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)

#logical operators
# and 
# or 
# not

# high_income = False
# good_credits = True
# student = True

# if high_income and good_credits:
#     print("eligible")
# else:
#     print("not eligible")
    
# if high_income or good_credits:
#         print("eligible")
# else:
#     print("not eligible")
    
# if not student:
#     print("eligible")
# else:
#     print("not eligible")

# if (high_income or good_credits) and not student:
#     print("eligible")
# else:
#     print("not eligible")


#Chaining comparison operators
# age = 22
# if 18 <= age <=65:
#     print("Eligible")



#For Loops
# for number in range(1, 4):
#    print ("Malmö University", number, number * "," )


#For esle
# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print ("Succesful")
#         break
# else:
#     print ("Attempted 3 times and failed")


#Nested Loop
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

#Iterables
# for x in "Python":
#     print(x)


#While loops 
# number = 100
# while number > 0:
#     print(number)
#     number //= 2
    
# command = ""
# while command != "quiet" and command != "QUIET":
#     command = input(">")
#     print("ECHO", command)

#Infinite Loop

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quiet":
#         break


#Exercise 

# for number in range(1, 100):
#     if number % 2 == 0:
#         print(number)   


#Defining Function 
# def greet():
#     print("Hello")
#     print("Nice to meet ya")


# greet()


#Arguments
# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Nice to meet ya")
    

# greet("Hassan", "Mousavi") 
# greet("Sasan", "Shahmehdi")       
    

#Different kind of functions
# def greet(name):
#     print(f"{name}")
    
# #Two types of functions: 
# # 1- Perfome a task 
# # 2- Return a value

# def get_greeting(name):
#     return f"Hi {name}"

# message = get_greeting("Hassan")
# print (message)

# file = open ("content.txt", "w")
# file.write(message)

#Ketword Arguments
#optional prameters should come after require prameters

# def increment(number, by):
#     return number + by

# print(increment(2, by=1))

#Default Argument
# [1, 2, 3, 4, 5]

# def multiply(*numbers):
#     print(numbers)
# multiply(2, 3, 4, 5)


#xargs
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
    
# print(multiply(2, 3, 4, 5))

##xargs 
# def save_user(**user):
#     print(user)
    
# save_user(id=1, name="Hassan", age="30")
 
 
#Debug
#Choose debug option by file then set a breakpoint by F9
#then start debugging by F5
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print("Start")
# print(multiply(1, 2, 3))


#Shortcuts are option and left and right arrows to move 
#copmletely to the right or left


#Exercise
# def fizz_buzz(input):
#     if input % 3 == 0:
#         return "Fizz"
#     else:
#         return "Buzz"

# print(fizz_buzz(15))

#Lists

# letters = ["a", "b", "c"]
# matrix = [[1, 2] [2, 3]]
# zeros = [0] * 5
# print(zeros)
# numbers = list(range(20))
# chars = list("Hello World!")
# print(chars)
# combine = zeros + letters
# print(combine)

#Accessoing Items
# letters = ["a", "b", "c", "d"]
# print(letters[0])
# #change the index so:
# letters [0] = "A"
# print(letters[0:3])
# numbers = list (range(20))
# print(numbers)
# #print every 2 elements
# print(numbers[::2])

#List unpacking
# numbers = [1, 2, 3, 4]
# first, second, third, fourth = numbers
# first, * other, last = numbers
# print(first, last)
# print(other)


#Loops over lists
letters =["a", "b", "c"]
for letter in enumerate (letters):
    print(letter[0])
    