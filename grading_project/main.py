# Imports
import random as r

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
    students = ["Alice", "Bob", "Charles", "James", "Dorothy", "Megan", "Oliver", "Samantha"]
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
    # else:
        print("Student and grade not added. Invalid input. Please try again.")
        return # return to main function
    
    

def main():
    # initialize project by generating students and their grades
    # and overwriting the grades.txt file with the students & their grades
    init_file_with_random_grades()
    display_grades_from_file()
    
    append_new_grades_to_file()
    
    
    
    
    
if __name__ == "__main__":
    main()
