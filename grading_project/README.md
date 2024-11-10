# Project: Student Grade Management System
## Project Overview
In this project you will create a python program that manages student grades. Your program will allow users to initialize a list of students with random grades. View all grades, add new grades, update existing grades, sort and display grades, and find the highest and lowest grades. You’ll use file handling to save and retrieve data, and each functionality will be implemented as a separate function.
## Project requirements
1.	File Management
    a.	Use a file called grades.txt to store student names and grades. 
    b.	Implement options to create, read, append, and update data in the file.
2.	Functions
    a.	Each functionality should be implemented in its own function.
    b.	The main menu should only handle calling these functions and returning data between them.
3.	Data Structures
    a.	Use lists to handle student data temporarily while processing and displaying information.
4.	User interface 
    a.	I implement a main menu that repeats until the user chooses to quit. 
    b.	After each menu selection, the screen should clear and return to the main menu to keep the interface organized.

# Step by step instructions
## Step 1: Set up File Initialization with Random Grades
Create a function that generates a list of students with random grades and writes them to grades,txt Use a small set of sample names (e.g. ‘Alice’, ‘Bob’, etc.), and assign each a random grade between 0 and 100. This function should overwrite the file each time it’s called.

## Step 2: Display grades from file
Create a function that reads grades.txt and displays all student names and gradesin the console. If the file doesn’t exist or is empty, display a message indicating that no grades are found.

## Step 3: Append New Grades to File
Develop a function that allows the user to add a new student and grade. Prompt the user for the students name and grade, and append this information to grades.txt.
## Step 4: Update an Existing Grade
Write a function to update a specific students grade.
1.	Read and store all the students and their grades from grades.txt
2.	Sort the list of students alphabetically and display them as a numbered menu.
3.	Allow the user to select a student by number and input a new grade.
4.	Update the grade for the selected student in the original list and overwrite grades.txt with the updated list
## Step 5: Sort Grades
Create a function to sort and displays grades in descending order without modifying the order in grades.txt. This function should:

1.	Read the student names and grades into a list.
2.	Sort the list by grade in descending order.
3.	Display the sorted grades.
## Step 6: Display highest and Lowest Grades
Develop a function that reads the grades from grades.txt, identifies the highest and lowest grades, and displays them.
## Step 7: Implement the Main Menu
Create `main_menu()` function that
1.	Displays options for each feature (Initialize, view grades, add grade, update grade, sort grade, highest/lowest grade, quit).
2.	Waits for the user’s input and calls the appropriate function based on their selection.
3.	Clears the screen after each operation and return to the main menu until the user selects ‘Quit’.
## Step 8: Test each function
After coding each function 
1.	Test it individually to ensure it works correctly.
    a. Check that the program handles errors gracefully, such as non-existent files, invalid inputs, and out of range selection’s

# Project completion checklist:
•	**File Operations**: Can create, append, read, and update the grades.txt file
•	**Random Generation**: Generates random grades for sample students when installing the file.
•	**User Interface**: Includes a main menu that loops until the user decides to quit, with the screen clearing after each operation to keep the interface organized.
•	**Data Processing**: Properly reads, sorts, and updates student data without altering the order in the original file for certain operations.
•	**Error Handling**: Includes handling for invalid inputs, such as non-existent files, out-of-range selections , and non-numeric inputs where applicable.
Final Notes
•	**Comments and Code Readability**: Ensure that each function is well documented. Write comments explaining what each function does, including any assumptions about the data.
•	**Modularity**: Your code should be modular, meaning each function only performs one specific task. This will make your code more organized and easier to debug or modify.
•	**Testing**: Test each menu option multiple times to verify that all functions work as expected and handle errors gracefully.