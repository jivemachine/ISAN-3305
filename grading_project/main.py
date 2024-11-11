# Imports
import random as r

# STEP 1
# function generates a random number between 0-100 and returns
# the number to bs used by the generate students
# function
def generate_grade(): 
    # generate a random number between 0-100
    grade = r.randint(0, 100)
    # return the random number
    return grade


# function generates a list of 8 students and randomizes their grades
def generate_students():
    # List of 8 students
    students = ["Zhang", "Alice", "Bob", "Charles", "James", "Dorothy", "Oliver", "Samantha"]
    # List comprehensio to generate a list of 8 random grades
    grades = [generate_grade() for i in range(8)]
    # Zip the two lists together
    student_grades = list(zip(students, grades))
    
    # return the list of the students with their grades
    return student_grades
    

# Function inputs a list of students and overwrites the grades.txt file 
# with the contents of students and their grades
# from the generate students function
def overwrite_txt_file(student_grades):
    with open("grades.txt", "w") as f:
        for student in student_grades:
            f.write(f"{student[0]}: {student[1]}\n")
            
# function uses generates students and overwrites the grades.txt file 
# with the contents of the students names and their randomly generated grades
def init_file_with_random_grades():
    student_list = generate_students()
    overwrite_txt_file(student_list)
  
# STEP 2          
# function reads the grades.txt file and displays the students names
# as well as their grades from the file
def display_grades_from_file():
    # file name contains the students and their grades
    file = "grades.txt"
    # check if file exists
    try:
        with open(file, "r") as f:
            # if file exists check if it is empty
            if f.read() == "":
                print("No grades found.") # if empty print error message
                return # return to main function
            else:
                # display the students and their grades from file
                f.seek(0) # move read 'cursor' to the beginning of file
                print(f.read()) # read and print the contents of the file to terminal      
    # if file does not exists print error message
    except FileNotFoundError:
        print("No grades found.")
        return # return to main function

# STEP 3
# function asks user to input a student name and grade
# and validtes the inputs to ensure referential integrity within the file
def get_user_new_student_and_grade():
    # get user input for student name
    student_name = input("Enter student name: ")
    # sanitize string input by removing leading and trailing white spaces
    student_name = student_name.strip()
    # capitalize first letter of string
    student_name = student_name.capitalize()
    # validate that input is a string
    if not student_name.isalpha():
        print("Student name is invalid.")
        return None, None # if string is not valid return None, None to append_student_grades function
    
    # get user grade for student
    student_grade = input("Enter student grade: ")
    # sanitize integer input by removing leading and trailing white spaces
    student_grade = student_grade.strip()
    # validate if student grade is a number
    try:
        student_grade = int(student_grade)
    except ValueError:
        print("Grade must be a number.")
        return None, None # if grade is not valid return None, None to append_student_grades function
    
    return student_name, student_grade # return student name and grade to append_student_grades function
    

# function inputs a student and grade append single student and grade to existing grades.txt file
def append_student_grades(student_name, student_grade):
    file = "grades.txt"
    with open(file, "a") as f:
        f.write(f"{student_name}: {student_grade}\n")


    
# function allows user to add new students and their grades to the grades.txt file
def append_new_grades_to_file():
    # ask user to input student name and grade to append to file
    student, grade = get_user_new_student_and_grade()
    # if student and grade are not None append student and grade to file
    if student and grade:
        append_student_grades(student, grade)
        return # return to main function
    else:
        print("Student and grade not added. Invalid input. Please try again.")
        return # return to main function
    
# STEP 4
# function reads grades.txt and returns a list of students and their grades
def read_grades_from_file():   
    # file name that contains students and grade data
    file = "grades.txt"
    # read the file and store contents in a list
    try:
        with open(file, "r") as f:
            # read the contents of the file
            data = f.readlines()
            # create an empty list to store the students and their grades
            student_grades = []
            # go through data and split the student name and grade
            for line in data:
                # split the line into student name and grade
                name, grade = line.split(":")
                # append the student name and grade to the list
                student_grades.append((name.strip(), int(grade.strip())))
            # return the list of students and their grades
            return student_grades
    # if file does not exist print error message
    except FileNotFoundError:
        print("No grades found.")
        return None
   
# function inputs a list of students and their grades and sorts 
# them by the name alphabetically as a numbered menu   
def display_sorted_grades(student_grades):
    # sort the students by name alphabetically
    student_grades.sort()
    # create a menu for the students
    for i, student in enumerate(student_grades, 1):
        print(f"{i}. {student[0]} - {student[1]}")
    
# get student to update from user input
def get_student_to_update(index):
    # get user input for student name
    student = input("Enter number for student to update: ")
    # sanitize string input by removing leading and trailing white spaces
    student = student.strip()
    # validate if student is a number
    try:
        student = int(student)
    except ValueError:
        print("Student number is invalid.")
        return None # if student is not valid return None to update_student_grade function
    
    # validate if student number is within the range of the students
    if student < 1 or student > index:
        print("Student selected tom update is invlaid.")
        return None
    return student # return student number to update_student

# get new grade from user input
def get_new_grade():
    # get user grade for student
    student_grade = input("Enter new student grade: ")
    # sanitize integer input by removing leading and trailing white spaces
    student_grade = student_grade.strip()
    # validate if student grade is a number
    try:
        student_grade = int(student_grade)
    except ValueError:
        print("Grade must be a number.")
        return None # if grade is not valid return None to update_student_grade function
    
    return student_grade # return student grade to update_student_grade

# function updates the grade of a student in the grades.txt file
def update_student_grade():
    # get grades from grades.txt file
    student_grades = read_grades_from_file()
    # if grades are not found return to main_menu
    if student_grades is None:
        return 
    # display the students and their grades
    display_sorted_grades(student_grades)
    # get the student to update
    student = get_student_to_update(len(student_grades))
    # if student is not valid return to main function
    if student is None:
        return
    # get the new grade for the student
    grade = get_new_grade()
    # if grade is not valid return to main function
    if grade is None:
        return
    # update the grade of the student
    student_grades[student - 1] = (student_grades[student - 1][0], grade)
    # overwrite the grades.txt file with the updated student grade
    overwrite_txt_file(student_grades)
    
# STEP 5
# function sorts grades in ascending order using basic sorting algorithm
def sorter(student_grades):
    for i in range(len(student_grades)): # gets each individual student tuple from student_grades list
        for j in range(len(student_grades) - 1): # gets the grades from the student tuple
            if student_grades[j][1] < student_grades[j + 1][1]: # compares grade of student to grade of next student
                student_grades[j], student_grades[j+1] = student_grades[j+1], student_grades[j] # swaps the students if the grade is less than the next students grade
    # return the sorted student grades
    return student_grades

# function displays the students and their grades
def display_data(student_grades):
    for student in student_grades:
        print(student)

# function sorts grades in descending order in grades.txt file
def sort_grades_descending():
    # get student data from read_grades_from_file_funcxtion from step 4
    student_grades = read_grades_from_file()
    # if no grades are found return to main menu
    if student_grades is None:
        return 
    # sort the students by grade in descending order
    student_grades = sorter(student_grades)
    # display grades to user
    display_data(student_grades)
    return 
            
  
# STEP 6
# function displays the highest and lowest grades in grades.txt file
def display_highest_and_lowest_grades():
    # get student data from read_grades_from_file function from step 4
    student_grades = read_grades_from_file()
    # if no grades are found return to main menu
    if student_grades is None:
        return
    # sort the students by grade in descending order using sorter from step 5
    student_grades = sorter(student_grades)
    # display the highest and lowest grades
    print(f"Highest grade: {student_grades[0][0]} - {student_grades[0][1]}") # highest grade will be in first index
    print(f"Lowest grade: {student_grades[-1][0]} - {student_grades[-1][1]}") # lowest grade will be in last index
    return         
      
      
# STEP 7
# function is a main menu that displays the options to the user
def main_menu_UI():  
    print("1. Initialize data")
    print("2. View Grades")
    print("3. Add Grade")
    print("4. update grade")
    print("5. sort grades")
    print("6. Display Highest and Lowest grades")
    print("7. Exit application")
    
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

# function clears terminal to keep the application interface clean
def clear_terminal():
    print("\033[H\033[J")


# function is the main function that runs the application
def main_menu():    
    # main menu loop
    while True:
        # display the main menu
        main_menu_UI()
        # get user input for the main menu
        user_input = get_user_input()
        # if user input is not valid return to main menu
        if user_input is None:
            continue
        # if user input is 1 initialize data
        if user_input == 1:
            clear_terminal() # clear terminal screen
            init_file_with_random_grades()
        # if user input is 2 view grades
        elif user_input == 2:
            clear_terminal() # clear terminal screen
            display_grades_from_file()
        # if user input is 3 add grade
        elif user_input == 3:
            clear_terminal() # clear terminal screen
            append_new_grades_to_file()
        # if user input is 4 update grade
        elif user_input == 4:
            clear_terminal() # clear terminal screen
            update_student_grade()
        # if user input is 5 sort grades
        elif user_input == 5:
            clear_terminal() # clear terminal screen
            sort_grades_descending()
        # if user input is 6 display highest and lowest grades
        elif user_input == 6:
            clear_terminal() # clear terminal screen
            display_highest_and_lowest_grades()
        # if user input is 7 exit application
        elif user_input == 7:
            print("Thank you for using the application!")
            break

def main():
    # main menu function runs the whole script
    main_menu()
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
