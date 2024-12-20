

# globals
global FILE
FILE = "expense.txt"

def load_expense_report(FILE):
    try:
        with open(FILE, "r") as f:
            expense_dictionary = {}
            # for line in f:
            #     category, amount = line.strip().split(",")
            #     expense_dictionary[category] = amount
            #     print(category, amount)
            if f.read() == "": # empty
                print("Expense report is empty.")
                expense_dictionary = {}
                return expense_dictionary
            else:
                expense_dictionary = {}
                f.seek(0)
                for line in f:
                    category, amount = line.strip().split(",")
                    expense_dictionary[category.strip()] = int(amount)      
            return expense_dictionary
    except FileNotFoundError:
        print("No expense report found")
        expense_dictionary = {}
        return expense_dictionary
            
def main_menu_UI():  
    print("1. Add/Update Expense")
    print("2. View Expense")
    print("3. Show total expense")
    print("4. Exit application")  



def add_or_update_expense(data):
    category = input("Select an expense category: ")
    
    category = category.strip()
    category = category.lower()
    if not category.isalpha():
        print("Category is not valid")
        return data
    
    amount = input("input an amount: ")
    amount = amount.strip()
    try:
        amount = int(amount)
        if amount < 0:
            print("Amount must be > 0")
            return data
    except ValueError:
        print("Amount must be a number.")
        return data

    data[category] = amount
    print(data)
    return data
    

def view_data(data):
    categories = list(data.keys())
    for category in categories:
        print(f"Category: {category}, Amount: {data[category]}")


def show_total_expense(data):
    total = 0
    for i in data:
        total += int(data[i])
    print(f"Total of all expenses: {total}")


def exit_and_save(data):
    categories= list(data.keys())
    with open(FILE, 'w') as f:
        for category in categories:
            for i in data:
                f.write(f"{category},{data[i]}\n")


# function gets user input for the main menu
def get_user_input():
    # get user input for the main menu
    user_input = input("Enter number for option: ")
    # sanitize string input by removing leading and trailing white spaces
    user_input = user_input.strip()
    # validate if user input is a number
    try:
        user_input = int(user_input)
    except ValueError:
        print("Option selected is invalid.")
        return None # if user input is not valid return None to main function
    
    # validate if user input is within the range of the options
    if user_input < 1 or user_input > 7:
        print("Option selected is invalid.")
        return None
    return user_input # return user input to main function


# function is the main function that runs the application
def main_menu():    
    # main menu loop
    expense_report = load_expense_report(FILE)
    clear_terminal() # clear terminal screen
    while True:
        # display the main menu
        main_menu_UI()
        # get user input for the main menu
        user_input = get_user_input()
        # if user input is not valid return to main menu
        if user_input is None:
            clear_terminal() # clear terminal screen
            continue
        # if user input is 1 initialize data
        if user_input == 1:
            # clear_terminal() # clear terminal screen
            expense_report = add_or_update_expense(expense_report)
        # if user input is 2 view grades
        elif user_input == 2:
            # clear_terminal() # clear terminal screen
            view_data(expense_report)
            # display_grades_from_file()
        # if user input is 3 add grade
        elif user_input == 3:
            # clear_terminal() # clear terminal screen
            show_total_expense(expense_report)
        # if user input is 4 update grade
        elif user_input == 4:
            # clear_terminal() # clear terminal screen
            exit_and_save(expense_report)
            print("Thank you for using the application!")
            break


# function clears terminal to keep the application interface clean
def clear_terminal():
    print("\033[H\033[J")


def main():
    main_menu()
    

if __name__ == "__main__":
    main()