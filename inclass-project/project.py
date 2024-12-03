import os
import random as r
from datetime import datetime


def load_file():
    # display titles of all files in 0_input directory
    files = os.listdir("0_input")

    # make sure there are files present in folder
    if len(files) == 0:
        # exit function if no files are present
        print("No files found in 0_input directory.")
        log_error(f"{generate_timestamp()} - No files found in 0_input directory.")
        return None
    
    # display files
    for i, file in enumerate(files):
        count = 0
        # make sure file is csv or else do not display
        if file.endswith(".csv"):
            count += 1
            # title for menu only on first file
            if count == 1:
                print("Files in 0_input directory: ")
            
            # print file name
            print(f"{count}. {file}")
        else:
            # print and log error message that file is not a csv file with timestamp and file name
            print("File is not a csv file.")
            log_error(f"{generate_timestamp()} - {file} is not a csv file.")

    
    # get user input for file choice
    # user_choice = int(input("Enter the number associated with the file you would like to load: "))

    # error handling
    # while user_choice < 1 or user_choice > len(files):
    #     print("Invalid choice. Please try again.")
    #     user_choice = int(input("Enter the number associated with the file you would like to load: ")) 
    # # get file name
    # file = files[user_choice - 1]
    # print(file)


    # try:
    #     if os.path.exists(file):
    #         with open(file, "r") as f:
    #             # get headers
    #             # headers = f.readline().strip().split(",")
    #             # get data
    #             data = f.readlines()
    #             # convert data to list of dictionaries
    #             # data = [dict(zip(row.strip().split(","))) for row in data]
    #         return data
    # except:
    #     print("Failed")

def log_error(message):
    # log error message to error.txt file in logs folder
    
    # check if logs folder exists within directory
    if os.path.exists('logs'):
        with open("logs/errors.txt", "a") as f:
            f.write(f"{message}\n")
    else: # create logs folder if it does not exist
        os.mkdir("logs")
        with open("logs/errors.txt", "a") as f:
            f.write(f"{message}\n")

# generates timestamp for error messages
def generate_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def has_header():
    user_input = input("Does the first row contain header? y/n: ")
    if user_input.lower() == 'y':
        return True
    else:
        return False


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
    # while True:
        load_file()
        # display_menu()
        # choice = int(input("Enter your choice: "))
        # data = load_file()
        # print(data)
        # has_header = handle_menu_choice(choice, data, has_header)


if __name__ == "__main__":
    main()
