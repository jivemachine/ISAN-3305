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
        return None, False
    
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
        return None, False
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
                return None, False
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
                    return data, False # return data no headers set
            except:
                log_error(f"{generate_timestamp()},Issue loading file - {file}")
                print("Failed")
                # return None
        else: # for edge cases
            return None, False
    

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
    """Displays the first 50 rows of data in a table format similar to pandas head(50).
       It creates a visually appealing ASCII table.
    """
    if data is None:
        print("No data loaded. Please load a file first.")
        return data, False

    # Extract headers (keys of the dictionary)
    headers = list(data.keys())

    # If no data or headers are present
    if not headers:
        print("No data to display.")
        return data, False
    
    total_rows = len(data[headers[0]])
    if total_rows == 0:
        print("No data rows found.")
        return data, False

    # Configuration
    rows_to_display = min(50, total_rows)      # Display up to 50 rows
    max_headers = 10                           # Truncate if too many columns
    if len(headers) > max_headers:
        headers = headers[:max_headers]
        print("Warning: Too many columns to display. Showing only the first 10.")

    # Determine column widths
    # Width is based on the max length of the header or any of the values in the first 50 rows
    column_widths = {}
    for h in headers:
        # Consider the header length and the data lengths for the rows we are displaying
        max_data_length = max([len(str(data[h][i])) for i in range(rows_to_display)]) if rows_to_display > 0 else 0
        column_widths[h] = max(len(h), max_data_length)
    
    # A helper function to construct a horizontal line based on column widths
    def build_line():
        parts = []
        for h in headers:
            parts.append('-' * (column_widths[h] + 2))  # +2 for the spaces on each side
        return '+' + '+'.join(parts) + '+'

    # Build the header row
    def build_header_row():
        cells = []
        for h in headers:
            # Center align the header text within the column width
            cells.append(f" {h.center(column_widths[h])} ")
        return '|' + '|'.join(cells) + '|'

    # Build a data row given the index
    def build_data_row(idx):
        cells = []
        for h in headers:
            val = str(data[h][idx])
            # Left align the data for readability
            cells.append(f" {val.ljust(column_widths[h])} ")
        return '|' + '|'.join(cells) + '|'

    # Construct the table
    top_line = build_line()
    header_line = build_header_row()
    separator_line = build_line()

    # Print table
    print(top_line)
    print(header_line)
    print(separator_line)

    for i in range(rows_to_display):
        print(build_data_row(i))

    bottom_line = build_line()
    print(bottom_line)

    # If there are more rows than 50, print a note
    if total_rows > 50:
        print(f"\nOnly showing first 50 rows out of {total_rows} total rows.")

    # Wait for user input to return to the main menu
    input("Press Enter to return to the main menu...")
    return data, True
        





def handle_menu_choice(choice, data, has_header):
    """Handle the user's menu choice. Returns the updated data and header
    status."""
    if choice == 1:
        data, has_header = load_file()
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
        data, has_header = display_data(data)
        return data, has_header
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
