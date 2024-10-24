import random
import math
import turtle as t

# method 1
def get_netid_seed():
    student_id = input("Please enter your netID: ")
    seed = sum(ord(char) for char in student_id)
    random.seed(seed)
    return seed

# method 2
def roll_1_100(seed, dec=0):
    roll = random.randint(a=1, b=100)
    return roll

# method 3
def roll_5_total(seed, dec=0):
    total = 0
    for i in range(0, 5):
        total += roll_1_100(seed)
    print(f"total of 5 rolls: {total}.")
    return total

# method 4
def float_roll(seed):
    total = 0
    for i in range(0, 5):
        total += roll_1_100(seed) + random.random()
    
    # accumulate total
    #total = roll_1 + roll_2 + roll_3 + roll_4 + roll_5
    print(f"total of 5 float rolls: {total}.")
    return total

# method 5
def roll_difference(num1, num2):
    if num1 > num2:
        diff = num1 - num2
    else:
        diff = num2 - num1
    return diff

# method 6
def cat_msg(num1, num2):
    if num1 > num2:
        print("First number is the larger of the two.")
    elif num2 > num1:
        print("Second number is the larger of the two.")
    else:
        print("They're both the same number...")


 # method 7
def divise(numerator, denominator):
    divide = numerator / denominator
    return numerator, denominator, divide


# method 8
def describe(nume, deno):
    print(f"Numerator: {nume} & Denominator: {deno}")


# method 9
def draw():
    t.circle(25)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    

def main():
    myseed = get_netid_seed()
    total_5_rolls = roll_5_total(myseed)
    total_float_roll = float_roll(myseed)
    difference = roll_difference(total_5_rolls, total_float_roll)
    cat_msg(total_5_rolls, total_float_roll)
    num, den, divide = divise((total_5_rolls + total_float_roll), difference)
    describe(num, den)
    draw()
    
    

main()
