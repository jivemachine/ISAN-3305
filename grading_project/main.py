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
    student_grades = read_grades_from_file()
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

def main():
    # initialize project by generating students and their grades
    # and overwriting the grades.txt file with the students & their grades
    init_file_with_random_grades()
    display_grades_from_file()
    
    append_new_grades_to_file()
    update_student_grade()
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
