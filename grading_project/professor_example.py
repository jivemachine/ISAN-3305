# Imports
import random

def initialize_grades(): # Create Grades
    students = ["Alice", "Bob", "Charlie", "David", "Eve"]
    grades = [random.randint(0,100) for _ in students]
    
    with open("grades_example.txt", "w") as file:
        for student, grade in zip(students, grades):
            file.write(f"{student}, {grade}\n")
    print("Grades have been initialized with random values.")
    
def load_grades(): # Read Grades
    students = []
    grades = []
    
    try:
        with open("grades_example.txt", "r") as file:
            for line in file:
                student, grade = line.strip().split(",")
                students.append(student)
                grades.append(int(grade))
    except FileNotFoundError:
        print("No grades found. Initialize the file.")
    return students, grades
        
        
def display_grades(): # Show grades
    students, grades = load_grades()
    if not students: 
        print("No grades found.")
        return
    print("Current Grades:")
    for student, grade in zip(students, grades):
        print(f"{student}: {grade}")
    
def add_grade(): # Add grade
    student = input("Enter student's name: ")
    try:
        grade = int(input("Enter student's grade (0-100): "))
        if 0 <= grade <= 100:
            with open("grading_example.txt", "a") as file:
                file.write(f"{student}, {grade}")
            print(f"Added {student} with grade {grade}")
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid argument.")

def update_grade():
    students, grades = load_grades()
    if not students: 
        print("No grades found.")
        return
    print("Current grades:")
    for i, (student, grade) in enumerate(zip(students, grades), 1):
        print(f"{i}. {student}: {grade}")
    try:
        choice = int(input("Select the student number to update: "))
        if 1 <= choice <= len(students):
            new_grade = int(input("Enter a new grade (0-100): "))
            if 0 <= new_grade <= 100:
                grades[choice-1] = new_grade
                
                with open("grades_example.txt", "w") as file:
                    for student, grade in zip(students, grades):
                        file.write(f"{student}, {grade}\n")
                print(f"Updated the grades for {students[choice-1]} to {new_grade}")
            else:
                print("Grade must be between 0-100.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Plrsdr input a number.")
        
        
def sort_grades(): # sort grades
    students, grades = load_grades()
    if not students:
        print("No grades to sort.")
        return

    combined = list(zip(students, grades))
    combined.sort(key=lambda x: x[1], reverse=True)
    
    print("Grades sorted in descending order")
    for student, grade in combined:
        print(f"{student}: {grade}")
        
def highest_and_lowest_grades(): # highest score and lowest score
    students, grades = load_grades()
    if not students:
        print("No grades found.")
        return
    
    max_grade = max(grades)
    min_grade = min(grades)
    max_student = students[grades.index(max_grade)]
    min_student = students[grades.index(min_grade)]
    
    print(f"Highest grade: {max_student}: {max_grade}")
    print(f"Lowest grade: {min_student}: {min_grade}")
    
def main_menu():
    while True:
        print("\nStudent Grade managemnet system")
        print("1. Init Grades")
        print("2. View grades")
        print("7. Quit")
        
        choice = input("Choose please: ")
        if choice == "1":
            initialize_grades()
        elif choice == "2":
            display_grades()
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Pick a valid choice.")
    