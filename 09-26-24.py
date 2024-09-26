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
            user_input = float(input("I need a positive non-zero number: "))
            if user_input > 0:
                return user_input
            else:
                print("enter number > 0")

        except ValueError:
            print("invalid input, please enter a valid number")



def how_many_days():
    days = int(input("how many days are you collecting bugs?"))
    return days


def collect_bugs(day_num):
    while True:
        try:
            bugs = float(input("Enter # of bugs collected: "))
            if bugs > 0:
                return bugs
            else:
                print("enter more than 0 bugs")
        except ValueError:
            print("invalid input, please enter a valid number")


def display_total_bugs(bugs, days):
    print(f"Collected {bugs} bugs in {days} days")


def calc_bugs():
    total_bugs = 0
    days = how_many_days()
    for day in range(1, days+1):
        bugs_collected = collect_bugs(day)
        total_bugs += bugs_collected
        
    display_total_bugs(total_bugs, days)
        
    
    
    

def main():
    print("Bug Collector", end="\n")
    calc_bugs()



main()
#get_positive_non_input()
#display_pattern()
#accumulator()
#display_num()
#mul_1000()
#add_num()


