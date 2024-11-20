# Imports
import random as r # random library for generating grades
import os # to check if grades.txt exists

# GLOBAL VARIABLES
FILE = 'grades.txt'


# Step 1 Initialize Grades with Random Values
# Description:
# Create a function to generate sample student 
# data with random grades between 0 and 100. 
# Save this data to a file (grades.txt) using a CSV format (Name,Grade). 
# Each time this function is called, overwrite the file and reset the dictionary.
def init_program(): 
    # sample students dictionary
    students = {'Alica', 'Barbra', 'Cody', 'Evan', 'Fergie'}
    # add random grades between 0-100 to dictionary using list comprehension
    data = dict(zip(students, [r.randint(0,100) for _ in students]))
    
    # overwrite_txt_file overwrites grades.txt with contents of data dictionary
    overwrite_txt_file(data)
    return True

#  function overwrites grades.txt with contents of dictionary
def overwrite_txt_file(dictionary: dict, file = FILE) -> None:
    # overwrite file contents
    with open(file, "w") as f:
        # iterate through dictionary
        for row in dictionary:
            # write data to file 
            f.write(f"{row},{dictionary[row]}\n")
        return None

# Step 2 Display Grades
# Description:
# Create a function to read the grades from the file 
# into a dictionary and display the contents. 
# If the file doesn’t exist or is empty, display an appropriate message.
def read_grades():
    # empty dictionary
    data = {}
    # nested try blocks for error validation to read contents of grades.txt
    try:
        # first check if file exists 
        if os.path.exists(FILE):
            # check if file is blank
            try:
                # using os to check size of file
                if os.path.getsize(FILE) > 0:
                    # read contents
                    with open(FILE, "r", newline=None) as f:
                        # iterate through file
                        for line in f:
                            # get student and grade using split
                            student_grade = line.split(',')
                            # add to data dictionary
                            data[str(student_grade[0])] = int(student_grade[1])
                else:
                    print("ERROR: File appears to be empty.")
            except:
                print("ERROR: Something went wrong with getting file.")
        else:
            print("ERROR: File does not exist.")
    except:
        print("ERROR: Something went wrong with getting file.")
    finally:
        if data:
            # display dictionary
            print("Current Grades:")
            for student in data:
                print(f"{student}: {data[student]}")
  
# function loads student grades data from file and outputs the data as a dictionary
def load_data():          
    # empty dictionary
    data = {}
    # nested try blocks for error validation to read contents of grades.txt
    try:
        # first check if file exists 
        if os.path.exists(FILE):
            # check if file is blank
            try:
                # using os to check size of file
                if os.path.getsize(FILE) > 0:
                    # read contents
                    with open(FILE, "r", newline=None) as f:
                        # iterate through file
                        for line in f:
                            # get student and grade using split
                            student_grade = line.split(',')
                            # add to data dictionary
                            data[str(student_grade[0])] = int(student_grade[1])
                else:
                    print("ERROR: File appears to be empty.")
            except:
                print("ERROR: Something went wrong with getting file.")
        else:
            print("ERROR: File does not exist.")
            return False
    except:
        print("ERROR: Something went wrong with getting file.")
    finally:
        if data:
            return data  
        
             
# Step 3 Add New Grades
# Description:
# Prompt the user for a student name and grade. 
# Validate the grade and add it to the dictionary. 
# Save the updated dictionary back to the file.
def add_new_grades():
    # load dictionary 
    data = load_data()
    while data:
        # get user input for student name
        student_name = str(input("Enter student name: "))
        # sanitize string input by removing leading and trailing white spaces
        student_name = student_name.strip()
        # capitalize first letter of string
        student_name = student_name.capitalize()
    
        # validate that input is a string
        if not student_name.isalpha():
            print("Student name is invalid.")
            # return None to go back to main menu
            return False
    
        # get user grade for student
        student_grade = input("Enter student grade: ")
        # sanitize integer input by removing leading and trailing white spaces
        student_grade = student_grade.strip()
        # validate if student grade is a number & between 0-100
        try:
            student_grade = int(student_grade)
            if student_grade < 0 or student_grade > 100:
                print("ERROR: Grade must be between 0-100.")
                return False
            else: # overwrite file with new data
                # add name and grade to dictionary
                data[student_name] = student_grade
                # overwrite grades.txt
                overwrite_txt_file(data)
                print("New student and grade successfully added.")
                return False
        except ValueError:
            print("ERROR: Grade must be a number.")
            return False
        
       
        
#  Step 4 Update an Existing Grade
# Description:
# Allow the user to update the grade for an existing student. 
# Load the dictionary, let the user select a student, 
# update their grade, and save the updated dictionary back to the file.
def update_grade():
    # load dictionary from file
    data = load_data()
    
    # validating data exists
    while data:
    
        # display students with indexes for selection
        i = 0
        for row in data:
            i += 1
            print(f"{i}. Student: {row} | Grade: {data[row]}")
        
        # allow user to make a selection
        user_choice = input("Select student by using their index # to the left of their name: ")
        user_choice = user_choice.strip()
        if user_choice.isalpha():
            print("ERROR: User input cannot be a string!.")
            return False
        user_choice = int(user_choice)
        if user_choice >= 1 and user_choice <= len(data):
            # allow user to enter grade to update to
            student_grade = input("Enter student grade: ")
            # sanitize integer input by removing leading and trailing white spaces
            student_grade = student_grade.strip()
            # validate if student grade is a number & between 0-100
            try:
                student_grade = int(student_grade)
                if student_grade < 0 or student_grade > 100:
                    print("ERROR: Grade must be between 0-100.")
                    return False # exit update grade 
                else: 
                    # add indexes to every line in dictionary
                    index = user_choice - 1
                    count = 0
                    while True:
                        for student in data:
                            if count == index:
                                # add new grade to selected student
                                data[student] = student_grade
                                # overwrite grades.txt
                                overwrite_txt_file(data)
                                print("Student grade updated successfully!")
                                return False # exit while loop
                            elif count < index:
                                count += 1
                            elif count > index:
                                print("Error: Something went wrong.")
                                return False
            except ValueError:
                print("ERROR: Grade must be a number.")
                return False
        else:
            print(f"ERROR: Input must be within range of 1 and {len(data)}.")
            return False
        
        
# Step 5 Sort and Display Grades
# Description:
# Sort the grades in descending order and display them 
# without modifying the dictionary or the file.
def sort_and_display():
    # load data from file
    data = load_data()
    
    # sort in descending order
    sorted_dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    
    # display dictionary
    print("Current Grades:")
    for student in sorted_dict:
        print(f"{student}: {sorted_dict[student]}")
    
# Step 6 Display the Highest and Lowest Grades
# Description:
# Identify and display the student(s) with the highest and 
# lowest grades, handling ties appropriately.
def max_min_grades():
    # load data
    data = load_data()
    
    # get min and max grades
    min_grade_key = min(data, key=data.get)
    max_grade_key = max(data, key=data.get)
    print(f"Max grade: {max_grade_key} -> {data[max_grade_key]}\nMin Grade: {min_grade_key} -> {data[min_grade_key]}")
    

# Step 7 Main Menu with Loops
# Description:
# Implement a main menu that repeatedly displays options for all the 
# features until the user selects "Quit."
def main_menu():
    while True:
        print("1. Initialize data")
        print("2. View Grades")
        print("3. Add Grade")
        print("4. update grade")
        print("5. sort grades")
        print("6. Display Highest and Lowest grades")
        print("7. Exit application")
        
        # get user input for the main menu
        user_input = input("Select an option: ")
        # sanitize string input by removing leading and trailing white spaces
        user_input = user_input.strip()
        # validate if user input is a number
        try:
            user_input = int(user_input)
        except ValueError:
            print("Option selected is invalid.")
        
        # validate if user input is within the range of the options
        # if user_input < 1 or user_input > 7:
            # print("Option selected is invalid.")
            
        if user_input == 1:
            init_program()
        elif user_input == 2:
            read_grades()
        elif user_input == 3:
            add_new_grades()
        elif user_input == 4:
            update_grade()
        elif user_input == 5:
            sort_and_display()
        elif user_input == 6:
            max_min_grades()
        elif user_input == 7:
            print("Exiting program. Bye!")
            return False
        else:
            print("Error: Command not found")
            
            
        
      
            
            
def main():
    main_menu()
    
    
    
if __name__ == "__main__":
    main()