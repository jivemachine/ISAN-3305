import os
import random as r
from datetime import datetime
import time
import sys


def load_file():
    # display titles of all files in 0_input directory
    files = os.listdir("0_input")

    # make sure there are files present in folder
    if len(files) == 0:
        # exit function if no files are present
        print("No files found in 0_input directory.")
        log_error(f"{generate_timestamp()},No files found in 0_input directory")
        return None
    
    # display files
    file_count = 0 # counter for files
    for i, file in enumerate(files):
        # make sure file is csv or else do not display
        if file.endswith(".csv"):
            file_count += 1
            # title for menu only on first file
            if file_count == 1:
                print("Files in 0_input directory: ")
            # print file name
            print(f"{file_count}. {file}")
        else:
            # log error message that file is not a csv file with timestamp and file name
            log_error(f"{generate_timestamp()},{file} is not a csv file")
        
    # if 0 csv files are found exit function
    if file_count == 0:
        print("No csv files found in 0_input directory.")
        log_error(f"{generate_timestamp()},No csv files found in 0_input directory")
        return None
    # add option add end for user to quit program
    print(f"{file_count + 1}. Back to Main Menu.")

    # Get user choice and handle errors
    while True:
        # get user input for file choice
        user_choice = input("Enter the number associated with the file you would like to load: ")
        user_choice.strip() # strip whitepace

        # check if user input is a string
        if user_choice.isalpha():
            # error message if user choice is not an integer
            print("Invalid choice. Please try again.")
            log_error(f"{generate_timestamp()},User input is not an integer")
        elif user_choice.isnumeric(): # checking is input is an integer
            user_choice = int(user_choice)
            # check if user wants to quit first
            if user_choice == file_count + 1:
                print("Back to main menu.")
                return None
            elif user_choice < 1 or user_choice > file_count:
                # display error message if user choice is not within range
                print("Invalid choice. Please try again.")
                log_error(f"{generate_timestamp()},User input is out of range")
                continue
            else: # load file if user choice is valid
                # get file name
                file = files[user_choice - 1]
                message = f"{file} loading..."
                print_slow(message)
            
            try: # get data from file
                data = {} # empty dictionary to store data
                file = "0_input/" + file
                with open(file, "r") as f:
                    # get data assume there are no headers in dataset
                    for i, line in enumerate(f):
                        data[i] = line.strip()
                    print("File loaded.")
                    return data # return data
            except:
                log_error(f"{generate_timestamp()},Issue loading file - {file}")
                print("Failed")
                # return None
        else: # for edge cases
            return None 
    

# write error message to /logs/errors_on_input.csv
def log_error(message):
    # check if logs folder exists within directory
    if not os.path.exists('logs'):
        os.mkdir("logs") # create logs folder
        with open("logs/errors_on_input.csv", "w") as f: # create csv file
            f.write('id,timestamp,error_message\n') # write headers
            f.write(f"0,{message}\n") # write error message
    else:
        # check if file exists
        if os.path.exists("logs/errors_on_input.csv"):
            # get current error log id
            with open("logs/errors_on_input.csv", "r") as f:
                id = len(f.readlines())
            # write error message to file
            if id >= 0:
                with open("logs/errors_on_input.csv", "a") as f:
                    f.write(f"{id},{message}\n")
        else: # create file if it does not exist
            with open("logs/errors_on_input.csv", "w") as f:
                f.write('id,timestamp,error_message\n')
                f.write(f"0,{message}\n")
       

# generates timestamp for error messages
def generate_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# prints text slowly
def print_slow(input):
    for char in input:
        print(char, end='', flush=True)
        time.sleep(0.0)
    print() # move to next line

def set_header_row(data):
    """Set the header row for the data."""
    # display first 5 rows of data
    for i in range(5):
        print(f"{i+1}. {data[i]}")

    # get users choice
    choice = input("Would you like to set the first row as the header? (y/n): ")
    choice = choice.lower().strip()
    # if users selects yes reset data to use first row as header
    if choice == "y":
        all_values = []
        new_data = {}
        print("Setting header row...")
        for i in data:
            if i == 0:
                headers = data[i].strip().split(",")
                for i in headers:
                    new_data[i] = []
                print("Header rows set.")
                print_slow("Adding relative data...")
            else:
                values = data[i].strip().split(",")
                all_values.append(values)
        for i in range(len(headers)):
            for j in range(len(all_values)):
                new_data[headers[i]].append(all_values[j][i])
        print("Data added.")
        return new_data, True
    elif choice == "n":
        header_choice = input("Input which row would you like to set as the header (1-5): ")
        header_choice = header_choice.strip()
        if header_choice.isnumeric():
            header_choice = int(header_choice)
            if header_choice < 1 or header_choice > 5:
                print("Invalid choice. Back to main menu.")
                return data, False
            else: # user entered a valid choice
                all_values = []
                new_data = {}
                print("Setting custom header row...")
                for i in data:
                    if i == header_choice-1:
                        headers = data[i].strip().split(",")
                        for i in headers:
                            new_data[i] = []
                        print("Header rows set.")
                        print_slow("Adding relative data...")
                    else:
                        values = data[i].strip().split(",")
                        all_values.append(values)
                for i in range(len(headers)):
                    for j in range(len(all_values)):
                        new_data[headers[i]].append(all_values[j][i])
                print("Data added.")
                return new_data, True
        else:
            print("Invalid choice. Back to main menu.")
            return data, False
    else:
        print("Invalid choice. Back to main menu.")
        return data, False

def display_data(data):
    for i in data:
        print(data[i])


def handle_menu_choice(choice, data, has_header):
    """Handle the user's menu choice. Returns the updated data and header
    status."""
    if choice == 1:
        data = load_file()
        return data, has_header
    elif choice == 2:
        if data is None:
            print("No data loaded. Please load a file first.")
        elif has_header:
            print("Header row already set.")
            return data, has_header
        else:
            data, has_header = set_header_row(data)
            return data, has_header
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
        sys.exit()
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


def handle_menu():
    """Handle the main menu loop."""
    data = None
    has_header = False
    while True:
        display_menu()
        choice = input("Enter choice: ")
        choice.strip()
        if choice.isnumeric():
            choice = int(choice)
            data, has_header = handle_menu_choice(choice, data, has_header)
        else:
            print("Invalid choice. Please try again.")
            continue
        

def main():
    handle_menu()


if __name__ == "__main__":
    main()
