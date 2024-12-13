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


# function displays data to user in a table format, that allows for pagination for both rows and columns
def display_data(data):
    # handle no data
    if data is None:
        print("No data loaded. Please load a file first.")
        return data, False

    # get headers and determine total rows
    headers = list(data.keys())
    if not headers:
        print("No headers found in data.")
        return data, False

    total_rows = len(data[headers[0]])
    # handle no data in file
    if total_rows == 0:
        print("The loaded file contains no rows of data.")
        return data, False

    # config for displaying data
    rows_per_page = 50        # Number of rows displayed at once
    columns_per_page = 9      # Number of columns displayed at once
    max_column_width = 25     # Maximum width for each column

    # function truncates text using width
    def truncate(text, width):
        if len(text) > width:
            half = (width - 3) // 2
            return text[:half] + '...' + text[-half:]
        return text

    # function to calculates column width for specific headers
    def compute_column_widths(sub_headers, row_start=0):
        # sample rows to determine max width
        sample_count = min(rows_per_page, total_rows - row_start)
        column_widths = {}
        # loop through headers
        for header in sub_headers:
            if sample_count > 0:
                # get sample values
                sample_values = data[header][row_start:row_start+sample_count]
            else:
                sample_values = []

            # determine max length of data
            max_data_length = max((len(str(item)) for item in sample_values), default=0)
            # determine max length of header
            max_length = max(len(header), max_data_length)

            # set column width
            column_widths[header] = min(max_length, max_column_width)
        return column_widths # return column widths

    # function displays 'page' of data
    def display_page_of_data(column_start, row_start):
        # subset of columns and rows to display
        col_end = min(column_start + columns_per_page, len(headers))
        # get headers for current page
        current_headers = headers[column_start:col_end]

        # get rows to display
        row_end = min(row_start + rows_per_page, total_rows)
        # calculate column widths
        column_widths = compute_column_widths(current_headers, row_start)

        # print headers
        header_row = "| " + " | ".join(
            f"{truncate(h, column_widths[h]):{column_widths[h]}}" for h in current_headers
        ) + " |"
        print(header_row)
        print("-" * len(header_row))

        # print rows
        for i in range(row_start, row_end):
            row_str = "| " + " | ".join(
                f"{truncate(str(data[h][i]), column_widths[h]):{column_widths[h]}}" for h in current_headers
            ) + " |"
            print(row_str)

        print(f"\nDisplaying rows {row_start+1} to {row_end} of {total_rows} total; columns {column_start+1} to {col_end} of {len(headers)} total.")

    # pagination logic for columns and rows
    column_start = 0
    while column_start < len(headers):
        row_start = 0
        while row_start < total_rows:
            display_page_of_data(column_start, row_start)

            # If no more rows to show in this column set
            if row_start + rows_per_page >= total_rows:
                break

            # Ask user to go to next set of rows or quit
            user_input = input("Press Enter to see the next 50 rows, 'c' to change columns, or 'q' to quit: ").strip().lower()
            if user_input == 'q':
                # Quit entirely
                input("Press Enter to return to the main menu...")
                return data, True
            elif user_input == 'c':
                # Stop row pagination and move on to next columns
                break
            else:
                # Move to next set of rows
                row_start += rows_per_page

        # Move to next set of columns if there are any
        if column_start + columns_per_page >= len(headers):
            # No more columns to show
            break
        user_input = input("Press Enter to see the next set of columns or 'q' to quit: ").strip().lower()
        if user_input == 'q':
            input("Press Enter to return to the main menu...")
            return data, True
        column_start += columns_per_page

    # After finishing all columns/rows
    input("Press Enter to return to the main menu...")
    return data, True

# function counts counts unique data values for each column within dataset
# then the function counts occurances of those unique values
# then function sorts data numerically for numeric data or alphabetically for non numeric data
# then returns the data in a sorted list of ranges for each column
# output will be a multidimensional list like this:
#       Every dimension is a column from the dataset
#           And every dimension beyond that is a columns of sorted data from the dataset
#               Then every column is sorted in order numerically or alphabetically as a tuple with the unique value and count
# [
#     [ # column 1
#         [(12, 1), (13, 3), (14, 5)]
#     ],
#     [ # column 2
#         [("al", 4), ("bob",12), ("clarissa", 1)]
#     ]
#     etc... 
# ]
#
#
def count_for_ranges(data):
    # handle no data
    if data == None:
        print("No data loaded. Please load a file first.")
        return None, False
    
    # get headers and handle no header errors
    headers = list(data.keys())
    if not headers:
        print("No headers found in data.")
        return data, False

    print_slow('Sorting data...')
    # get unque values for all values for each column
    # sort the data alphabetically or numerically
    # return column data as a list
    def get_unique_values(header):
        # get unique value for header and returns a sorted list for header
        unique_values = list(set(data[header]))

        # iterate through all data in unique_values list and if all values are an instance of numeric data, sort numerically
        def is_numeric(array_list):
            def is_numeric_value(value):
                try:
                    float(value)
                    return True
                except ValueError:
                    return False

            return all(is_numeric_value(item) for item in array_list)

        if is_numeric(unique_values):
            unique_values.sort(key=float)
        else:
            unique_values.sort(key=str.lower)
        # return sorted data
        return unique_values
    
    # function counts instance of each value in column
    def count_unique_value(val, data):
        count = 0
        for i in range(len(data)):
            if data[i] == val:
                count += 1
        return count
    
    # create output and sort data according to if data is numerically or alphabetically
    columns = []
    for header in headers:
        # each unique header adds an extra empty array to columns array
        columns.append([
            (value, count_unique_value(value, data[header])) for value in get_unique_values(header)
        ])
    return columns # returns sorted data

# function displays data from count_for_ranges function
# for columns with more than 50 unique values only display first 50
def display_ranges(data_ranges, data, has_headers):
    # handle no data
    if data == None:
        print("No data loaded. Please load a file first.")
        return False

    # handle missing headers
    if not has_headers:
        print("No headers found in data. Set headers for file first.")
        return False

    # handle no data ranges
    if data_ranges == None:
        print("No data to display, run 'count for ranges' then try again")
        return False
    
    print_slow('Displaying data ranges...')
    print_slow("Data is formatted as 'Unique_value: distinct_appearances_in_dataset'")
    
    # get header names
    headers = list(data.keys())

    # config
    max_display_rows = 50   # display at most 50 rows of unique values for each column
    max_column_width = 25   # max column width to prevent overly wide columns
    columns_per_page = 8    # number of columns to display at once

    # column widths
    def value_count_str(value, count):
        return f"{value}: {count}"
    
    # truncate string to fit width
    def truncate(text, width):
        if len(text) > width:
            #  long text will look like mcd...alds
            half = (width - 3) // 2
            return text[:half] + '...' + text[-half:]
        return text
    
    def format_cell(text, width):
        text = truncate(text, width)
        return f"{text:<{width}}"
    
    # paginating columns
    column_start = 0
    total_columns = len(headers)

    while column_start < total_columns:
        # get the num columns to display
        col_end = min(column_start + columns_per_page, total_columns)
        current_headers = headers[column_start:col_end]
        current_data_ranges = data_ranges[column_start:col_end]
        
        # how many rows we need to display (up to 50)
        max_length = max((len(col_data) for col_data in current_data_ranges), default=0)
        display_length = min(max_length, max_display_rows)

        # get column widths for these columns
        column_widths = []
        for i, header in enumerate(current_headers):
            longest_str_len = len(header)
            # up to display_length values
            for val, cnt in current_data_ranges[i][:display_length]:
                length = len(value_count_str(val, cnt))
                if length > longest_str_len:
                    longest_str_len = length
            # max col width
            if longest_str_len > max_column_width:
                longest_str_len = max_column_width
            column_widths.append(longest_str_len)

        # print the table
        header_row = "| " + " | ".join(
            format_cell(h, w) for h, w in zip(current_headers, column_widths)
        ) + " |"
        print(header_row)
        print("-" * len(header_row))

        # print rows
        for row_idx in range(display_length):
            row_cells = []
            for col_idx, header in enumerate(current_headers):
                col_data = current_data_ranges[col_idx]
                if row_idx < len(col_data):
                    val, cnt = col_data[row_idx]
                    cell_str = value_count_str(val, cnt)
                else:
                    cell_str = ""
                row_cells.append(format_cell(cell_str, column_widths[col_idx]))
            row_line = "| " + " | ".join(row_cells) + " |"
            print(row_line)
        
        print()  # \n

        if col_end < total_columns:
            # if there are more columns to display
            user_input = input("Press 'c' to view the next set of columns, or press Enter to return to the main menu: ").strip().lower()
            if user_input == 'c':
                column_start += columns_per_page
                print()  # add an extra line for readability
                continue
            else:
                break
        else:
            # no more left
            break

    # press enter to go home
    input("Press Enter to return to the main menu...")
    return True


def handle_menu_choice(choice, data, has_header, data_range=None):
    """Handle the user's menu choice. Returns the updated data and header
    status."""
    if choice == 1:
        data, has_header = load_file()
        return data, has_header, data_range
    elif choice == 2:
        if data is None:
            print("No data loaded. Please load a file first.")
        elif has_header:
            print("Header row already set.")
            return data, has_header, data_range
        else:
            data, has_header = set_header_row(data)
            return data, has_header, data_range
    elif choice == 3:
        data, has_header = display_data(data)
        return data, has_header, data_range
    elif choice == 4:
        data_range = count_for_ranges(data)
        return data, has_header, data_range
    elif choice == 5:
        display_ranges(data_range, data, has_header)
        return data, has_header, data_range
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
    data_range = None
    while True:
        display_menu()
        choice = input("Enter choice: ")
        choice.strip()
        if choice.isnumeric():
            choice = int(choice)
            data, has_header, data_range = handle_menu_choice(choice, data, has_header, data_range)
        else:
            print("Invalid choice. Please try again.")
            continue
        

def main():
    handle_menu()


if __name__ == "__main__":
    main()
