# imports
from datetime import datetime
import turtle as t

# 1
# User Input and Output
# Task: Create a program that asks the user for their name and then greets them with a personalized
# message.
# Instructions: Write a program that prompts the user to enter their name. After the user enters their
# name, display a message that includes their name in a friendly greeting


def user_input():
    print("What is your name? ")
    global name
    name = input()
    return name

def greeting():
    name = user_input()
    print(f"Hello, {name}")


# 2.
# Working with Variables
# Task: Assign values to variables and perform basic arithmetic.
# Instructions: Create variables to represent di􏰀erent pieces of data.
# Then, use those variables to perform simple arithmetic operations
# like addition, subtraction, multiplication, and division.
# Finally, display the results.

def inquire_numbers():
    print("What two numbers would you like to work with? [2 seperate inputs]")
    num1 = input()
    num2 = input()
    return num1, num2
    

def work(num1,  num2):
    add = int(num1) + int(num2)
    sub = int(num1) - int(num2)
    mul = int(num1) * int(num2)
    div = int(num1) / int(num2)
    return add, sub, mul, div

def _display(num1, num2, add, sub, mul, div):
    print(f"{num1} & {num2} added together = {add}")
    print(f"{num1} & {num2} subtracted = {sub}")
    print(f"{num1} & {num2} multiplied = {mul}")
    print(f"{num1} & {num2} divided = {div}")

def working_with_variables():
    num1, num2 = inquire_numbers()
    add, sub, mul, div = work(num1, num2)
    _display(num1, num2, add, sub, mul, div)


# 3.
# Comments in Code
# Task: Document your code with comments.
# Instructions: Write a program that includes at least three
# lines of code and add comments to explain what each part of the
# code does. Comments should describe the purpose of the
# code and any important details.

# this function asks the user to input their favorite band
def ask_fav_band():
    # ask for user input
    print(f"Whats your favorite band, {name}? ")

    # assigns users input to variable
    band = input()

    # function returns users input
    return str(band)

# compares users answer to array of bands
# if users favorite band is not in that list
# program tells them what it thinks of their musical taste
def is_band_good(your_favorite_band):
    # list of only good bands /s
    good_bands = ["metallica"]

    # strips spaces and lowercases string
    your_favorite_band = your_favorite_band.lower()
    your_favorite_band = your_favorite_band.replace(" ", "")

    # for loops through each band in good_bands array 
    for band in good_bands:
        # if statment dictates wether users music tastes are good or bad
        if your_favorite_band in band:
            print("RIDE THE LIGHTNING!!!")
        else:
            print("lol....your music sucks")


# this function puts the last 2 functions together
def _bands():
    band = ask_fav_band()

    return is_band_good(band)


# 4.
# String Operations
# Task: Combine multiple strings into a single message.
# Instructions: Write a program that takes two or
# more pieces of text and joins them together to a complete
# sentence. Display the combined text to the user.

def get_text():
    print("What's your favorite cuss word?")

    cuss_word = input()

    return cuss_word


def _concat():
    word = get_text() + name
    print(f"{word} lol")

# 5.
# Type Conversion
# Task: Convert user input into di􏰀erent data types.


def ask_user_for_data():
    print("Give me an integer")
    integer = input()

    return str(integer)

def perform_ops(string):
    return string + string

def _conversion():
    string = ask_user_for_data()
    print(f"converting integer into a string and added it together: {perform_ops(string)}")


# 6.
# Arithmetic Operations with Real Numbers
# Task: Perform calculations with decimal numbers.
# Instructions: Write a program that calculates the price of an
# item after adding sales tax. Ask the user for the price of the item,
# calculate the total cost after adding a percentage for tax, and
# display the final amount.

def get_price():
    print("How much is your item?")
    price = input()
    return float(price)

def get_sales_tax(price):
    tax = price * 0.0825
    return float(tax)

def total():
    price = get_price()

    tax = get_sales_tax(price)

    total = price + tax
    print(f"Item price: ${round(price,2)}")
    print(f"Tax for item: ${round(tax, 2)}")
    print(f"Total cost for item: ${round(total, 2)}")



# 7. Understanding Order of Operations
# Task: Calculate expressions with multiple operations.
# Instructions: Write a program that performs a calculation
# involving addition, multiplication, and parentheses. Explore how
# changing the order of operations (using parentheses) a􏰀ects the result.
def operations():
    num1 = 20
    num2 = 15
    num3 = 10
    num4 = 5
    add = num1 + num2
    sub = num3 - num4
    par = (num1 + num2) * (num3 - num4)
    print(f"Numbers used: {num1}, {num2}, {num3}, {num4}")
    print(f"Addition of {num1} & {num2}: {add}")
    print(f"subtraction of {num3} & {num4}: {sub}")
    print(f"order of operations: ({num1} + {num2}) * ({num3} - {num4}) = {par}")


# 8. Documenting Code
# Task: Explain your program with comments.
# Instructions: Write a program that performs a simple
# task and includes comments to describe what each section
# of the program does. Your comments should explain the overall
# purpose of the program as well as individual lines of code.

def ask_for_condiments():
    # prompt asks user what condiment they want on their hotdog
    print("What condiment would you like on your hotdog?")

    # stores input into condiment variable
    condiment = input()

    # prints users name from name global variable & displays what they
    # want on their hotdog
    print(f"{name}, wants {condiment} on their hotdog!")




# 9. Creating Functions
# Task: Define a function that performs a calculation.
# Instructions: Create a function that takes two numbers
# as input and returns the result of a mathematical operation
# (e.g., multiplication or division). Call this function from your
# main program and display the result.

def get_2_numbers():
    print("what number do you want to know the iterated exponent of?")
    num = int(input())

    iterated_exp = num**num
    print(f"{num} to the {num} power is {iterated_exp}")


# 10. Using Constants in Calculations
# Task: Calculate an area using a constant.
# Instructions: Write a program that calculates the area
# of a circle. Define a constant for the value of pi,
# ask the user for the radius of the circle, and use the
# formula for the area of a circle to calculate and display the result.

def pi():
    PI = 3.14
    return float(PI)

def get_radius():
    print("What is the radius for your circle?")
    rad = input()
    return int(rad)

def calculate_area_of_circle():
    r = get_radius()
    r = r**2
    area = pi() * r
    print(f"Area of your circle is {area}")



# 11. Combining Arithmetic and Variables
# Task: Use variables to store data and perform calculations.
# Instructions: Create a program that asks the user for two
# measurements (like length and width) and then calculates an
# area or perimeter. Display the result to the user.

def get_l_w():
    print("We need two measurements from you")
    print("Whats is the length: ")
    l = input()
    print("Now, what is the width?")
    w = input()
    return int(l), int(w)

def calc_perimeter():
    l,w = get_l_w()
    per: int = 2 * (l+w)
    print(f"the perimeter of your rectangle is {per}")
    



# 12. Building Dynamic Text
# Task: Create a program that generates personalized messages.
# Instructions: Write a program that combines user input with
# preset text to create a personalized message.
# For example, generate a welcome message that includes the user's
# name or favorite color.

def get_time():
    return datetime.now()

def inquire_fav_color():
    print("what is your favorute color?")
    color = input()
    return color

def day_n_night(time):
    today12pm = time.replace(hour=12, minute=0, second=0, microsecond=0)
    if time > today12pm:
        print(f"good afternoon, {name}")
    else:
        print(f"good morning, {name}")

    



def personalized_text():
    time = get_time()
    day_n_night(time)


# 13. Gathering Input from Users
# Task: Create a program that interacts with the user.
# Instructions: Design a program that asks the user a
# series of questions, gathers their responses, and then
# displays those responses in a summary format.

def questions():
    questions = ["What is your pets name?", "What city were you born?", "What year were you born?"]
    answers = []
    for q in questions:
        print(q)
        a = input()
        answers.append(a)
    return answers

def summary():
    a = questions()
    a1 = a[0]
    a2 = a[1]
    a3 = a[2]
    print(f"okay, so your name is {name}, your pets name is {a1}, you were born in {a3}, and your birthplace is {a2}?")
    print(f"I just stole your identity, {name}")


# 14. Creating and Using Functions
# Task: Break down your program into smaller tasks using functions.
# Instructions: Write a program that performs a task by
# calling a function. Ensure the function returns a value
# that is used elsewhere in the program.

def using_funcs():
    l,w = get_l_w()
    print(f"{l} times {w} times {pi()} = {int(l)*int(w)*pi()}")


# 15. Introduction to Turtle Graphics
# Task: Draw basic shapes using turtle graphics.
# Instructions: Use a turtle graphics library to draw simple
# shapes like squares, triangles, or lines. Control the turtle’s
# movement to create patterns or designs on the screen.

def draw_square():
    t.forward(20) 
    t.left(90) 
    t.forward(20)
    t.left(90)
    t.forward(20) 
    t.left(90) 
    t.forward(20)
    t.left(90)

def draw_circle():
    t.circle(20)

def drawing():
    draw_square()
    draw_circle()

# 16. Drawing Complex Shapes
# Task: Create a design using loops and turtle graphics.
# Instructions: Write a program that uses loops to repeat
# drawing commands with the turtle graphics library. Create a
# complex shape, such as a star or a polygon, by repeating simple movements.

def complex_shape():
    i = 0
    while i < 20:
        draw_circle()
        t.forward(20)
        i+=1
        if i >= 16:
            t.left(90)
            t.forward(50)
            t.color("blue")
        elif i >= 10:
            t.right(90)
            draw_square()
            t.forward(50)
            i+=1
        
# 17. Customizing Turtle Graphics
# Task: Change the appearance of your turtle drawings.
# Instructions: Modify your turtle program to use di􏰀erent
# colors for the pen. Experiment with lifting the pen to create
# designs with unconnected lines.


def weird_color_shape():
    i = 0
    while i < 20:
        draw_circle()
        t.forward(20)
        i+=1
        if i % 2 == 0:
            t.penup()
        else: t.pendown()

        if i % 5 == 0:
            t.color("red")
            t.begin_fill()
        else:
            t.end_fill()
        
        if i >= 16:
            t.left(90)
            t.forward(50)
            t.color("blue")
        elif i >= 10:
            t.right(90)
            draw_square()
            t.forward(50)
            i+=1    


# 18. Moving the Turtle Without Drawing
# Task: Move the turtle to di􏰀erent locations without drawing.
# Instructions: Write a program that uses turtle graphics to
# move the turtle to di􏰀erent parts of the screen without drawing.
# Then, have the turtle draw only in specific areas.

def new_spot():
    t.penup()
    t.left(90)
    t.forward(150)
    t.pendown()

def mickey_side_profile():
    t.home()
    
    t.color("blue")
    t.begin_fill()
    t.penup()
    t.forward(25)
    t.pendown()
    t.circle(10)
    t.penup()
    #t.left(90)
    t.forward(20)
    t.pendown()
    t.circle(10)
    t.penup()
    t.right(180)
    t.penup()
    t.forward(20)
    t.pendown()
    t.circle(20)
    t.end_fill()


def main():
    # 1.)
    greeting()

    # space for aesthetics
    print("\n")
    
    # 2.)
    working_with_variables()

    # space for aesthetics
    print("\n")

    # 3.)
    _bands()

    # space for aesthetics
    print("\n")

    # 4.)
    _concat()

    
    print("\n")

    # 5.)
    _conversion()

    print("\n")

    # 6.)
    total()

    print("\n")

    # 7.)
    operations()

    print("\n")

    # 8.)
    ask_for_condiments()

    print("\n")

    # 9.)
    get_2_numbers()

    print("\n")

    # 10.)
    calculate_area_of_circle()

    print("\n")

    # 11.)
    calc_perimeter()

    print("\n")

    # 12.)
    personalized_text()
    

    print("\n")

    # 13.)
    summary()

    print("\n")

    #14.)
    using_funcs()

    print("\n")

    # 15.)
    drawing()
    


    print("\n")

    # 16.)
    complex_shape()


    print("\n")


    #17.)
    weird_color_shape()


    print("\n")

    # 18.)
    mickey_side_profile()
        
    
    
    


main()
