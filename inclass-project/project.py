import os
import random as r


def load_file(file = "Student_Depression_Dataset.csv"):
    try:
        if os.path.exists(file):
            with open(file, "r") as f:
                # get headers
                headers = f.readline().strip().split(",")
                # get data
                data = f.readlines()
                # convert data to list of dictionaries
                data = [dict(zip(row.strip().split(","))) for row in data]
            return data
    except:
        print("Failed")

def has_header():
    user_input = input("Does the first row contain header? y/n: ")
    if user_input.lower() == 'y':
        return True
    else:
        return False


data = load_file('Practice Data for Synthetic.csv')


def handle_menu_choice(choice, data, has_header):
    """Handle the user's menu choice. Returns the updated data and header
    status."""
    if choice == 1:
        data = load_file()
    elif choice == 2:
        if data is None:
            print("No data loaded. Please load a file first.")
        else:
            has_header = set_header_row(data)
    elif choice == 3:
        display_data(data)
    elif choice == 4:
        count_for_ranges(data, has_header)
    elif choice == 5:
        display_ranges(data)
    elif choice == 6:
        data = roll_data(data)
    elif choice == 7:
        write_file(data)
    elif choice == 8:
        check_values(data)
    elif choice == 9:
        print("Exiting program. Goodbye!")
        return None, has_header
    else:
        print("Invalid choice. Please try again.")
        return data, has_header

def display_menu():
    """Display the main menu to the user."""
    print("\nMain Menu:")
    print("1. Load File")
    print("2. Header Row")
    print("3. Display Read Data")
    print("4. Count For Ranges")
    print("5. Display Ranges")
    print("6. Roll Data")
    print("7. Write File")
    print("8. Check Values")
    print("9. Exit")



def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        data, has_header = handle_menu_choice(choice, data, has_header)
