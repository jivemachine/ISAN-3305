def mul_1000():
    product = 0
    while product < 1000:
        try:
            user_input = float(input("enter a number: "))
            product = user_input * 10
            print(f"number is {user_input} product is {product}")
        except ValueError:
            print(f"please enter a valid number")


def add_num():
    while True:
        try: 
            num1 = float(input("Enter number 1: ")) 
            num2 = float(input("Enter number 2: "))
            total = num1+num2
            print(f"The sum of {num1} and {num2} is {total}")
            again = input("Do you want to performt he operation again? (yes/no) ").strip().lower()
            if again != 'yes':
                break
        except ValueError:
            print("error try agaain")



def display_num():
    for i in range(0, 101, 2):
        print(i, end=", ")


def accumulator():
    i = 0
    while i < 9:
        print(i)
        i += 1
    



        
def display_pattern():
    for _ in range(5):
        for _ in range(10):
            for _ in range(15):
                print("#", end="")    
            print()
        print()
        
    
def get_positive_non_input():
    while True:
        try:
        except ValueError:
            print("invalid input, please enter a valid number")


#display_pattern()
#accumulator()
#display_num()
#mul_1000()
#add_num()


