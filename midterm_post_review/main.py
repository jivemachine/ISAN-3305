import random
#import math
#import turtle as t

# method 1
def get_netid_seed():
    student_id = input("Please enter your netID: ")
    seed = sum(ord(char) for char in student_id)
    random.seed(seed)
    return seed


# what i did

# method 2
# def roll_1_100(seed, dec=0):
#     roll = random.randint(a=1, b=100)
#     return roll

# method 2
# What professor did 
def roll_one_integer(seed):
    return random.randint(1, 100)


# what i did for method 3
# def roll_5_total(seed, dec=0):
#     total = 0
#     for i in range(0, 5):
#         total += roll_1_100(seed)
#     print(f"total of 5 rolls: {total}.")
#     return total
        
        
def roll_five_integers(seed):
    random.seed(seed)
    total = 0
    for _ in range(5):
        total += random.randint(1, 100)
    return total
 
# what i did method 4
# def float_roll(seed):
#     total = 0
#     for i in range(0, 5):
#         total += roll_1_100(seed) + random.random()
    
#     # accumulate total
#     #total = roll_1 + roll_2 + roll_3 + roll_4 + roll_5
#     print(f"total of 5 float rolls: {total}.")
#     return total


def roll_five_floats(seed):
    random.seed(seed)
    total = 0
    for _ in range(5):
        total += random.uniform(1, 100)
    return total


# what i did for method 5
# def roll_difference(num1, num2):
#     if num1 > num2:
#         diff = num1 - num2
#     else:
#         diff = num2 - num1
#     return diff
def calculate_difference(value1, value2):
    if value1 > value2:
        return value1 - value2
    else:
        return value2 - value1


# what i did method 6
# def cat_msg(num1, num2):
#     if num1 > num2:
#         print("First number is the larger of the two.")
#     elif num2 > num1:
#         print("Second number is the larger of the two.")
#     else:
#         print("They're both the same number...")

def compare_total_value(value1, value2):
    if value1 > value2:
        return f"The first value is ({value1}) is larger than the second value ({value2})"
    else:
        return f"The second value is ({value2}) is larger than the first value ({value1})"

 # what i did for method 7
# def divise(numerator, denominator):
#     divide = numerator / denominator
#     return numerator, denominator, divide

def perform_division(numerator, denominator):
    if denominator != 0:
        return numerator / denominator
    else:
        return "error: denominator cannot = 0"
    
# what i did method 8
# def describe(nume, deno):
#     print(f"Numerator: {nume} & Denominator: {deno}")

def display_results(numerator, denominator):
    divison_result = perform_division(numerator, denominator)
    if isinstance(divison_result, float):
        modulo_result = numerator % denominator
        print(f"The numerator is ({numerator}), the denominator is ({denominator}) ")
        print(f"The result is {divison_result} and the modulo is {modulo_result}")
    else:
        print(divison_result)

def main():
    seed = get_netid_seed()
    random_integer = roll_one_integer(seed)
    total_integers = roll_five_integers(seed)
    total_floats = roll_five_floats(seed)
    difference = calculate_difference(total_integers, total_floats)
    comparison_message = compare_total_value(total_integers, total_floats)
    print(comparison_message)
    numerator = total_integers + total_floats
    display_results(numerator, difference)
    
    
    
if __name__ == "__main__":
    main()