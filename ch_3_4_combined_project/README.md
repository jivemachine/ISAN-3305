# Assignment For ISAN 3305

## Prompt:
>You are part of a development team tasked with creating an automated system for managing a university’s event operations. This system will handle participant registration, capacity management, personalized greetings, and data analysis after the event. The program will need to be modular, with all tasks handled by separate methods.

>*Note: The main() function can only be used for calling methods and transferring data between them.*

 

## Program Structure Requirements:

- You must structure your program so that each part of the system is handled by its own method. The main() function should serve only to call these methods and handle data passing. No other logic or operations should be placed in main().

 

## Program Requirements:

**Your task is to build a Python program with the following features, structured as methods:**

 

### Part 1: Event Registration (Decision Structures)

- Method: register_participant()
This method handles user registration, validating the role (student, faculty, guest) and ensuring that only eligible participants register.

    - Input: User name, role (student, faculty, guest).

    - Output: Registration confirmation message.

    - **The method should also keep track of the number of registrants and prevent over-registration (maximum 100 attendees).**

- Method: validate_role(role)
This method will check whether the role entered is valid (student, faculty, or guest). If the role is invalid, it will prompt the user to re-enter.

    - Input: A string representing the user's role.

    - Output: A validated role (student, faculty, or guest).

- Method: check_guest_list(name)
Guests can only register if they are on a pre-defined guest list. This method will check the guest's name against the guest list.

    - Input: The name of the guest.

    - Output: A boolean value indicating whether the guest can register.

 

### Part 2: Attendance Tracking and Capacity Management (Boolean Logic and Loops)

- Method: manage_capacity()
This method tracks registrations and stops accepting new registrations once the event is full (100 participants).

    - *It will call register_participant() repeatedly, updating the number of students, faculty, and guests.*

    - Input: None (this method will interact with other methods).

    - Output: A final registration report once the event is full.

    - Use Boolean logic to display a summary:

  > "This event is student-heavy" if more than 75% of registrants are students.
"Faculty are showing strong interest" if more than 50% of registrants are faculty.
"Expect additional guest services" if there are more than 10 guests.
 

### Part 3: Custom Greetings (String Comparisons)

- Method: greet_participant(name)
Use string comparisons to check if the participant is a keynote speaker or the event chairperson, and display a custom greeting for each type of participant.

    > **Keynote speakers and the event chairperson should get special messages; other attendees will get a general welcome.**

  - Input: The participant's name.

  - Output: A personalized greeting message.

 

### Part 4: Sending Thank You Messages (Nested Decision Structures)

- Method: send_thank_you(name, role, registration_days)
This method will determine whether to send a thank-you message to participants based on their role and the time of registration.

#### Use nested decision structures:

> Students and faculty who register more than 7 days before the event get a thank-you email with a feedback form.
Those who register within 7 days are thanked but are asked to follow the event page for updates.
Guests do not receive a thank-you email unless they are keynote speakers.
Input: Name, role, and registration days before the event.

  - Output: The appropriate thank-you message.

 

### Part 5: Attendance Data Analysis (Loops with Accumulation)

- Method: collect_event_data()
This method asks how long each participant stayed at the event and accumulates this data.

    - Input: The time each participant stayed (in minutes).

    - Output: Total time, average time, and maximum time participants stayed.

    **Use loops to collect and calculate this data.**

 

### Part 6: Displaying Registration Stats (For Loop and Ranges)

- Method: display_registration_stats(student_count, faculty_count, guest_count)
This method will display a table showing the number of registrants from each category (students, faculty, guests), alongside the percentage of total attendees they represent.

    - Input: The count of students, faculty, and guests.

    - Output: A table displaying the category, registrants, and percentage of total participants.

    **Use a for loop to iterate through each category and calculate the percentage.**

 


| Category |  Registrants |     Percentage |
| --------- | ----------- | ---------------- |
| Students |        60    |          60%    |
| Faculty  |        30     |        30%     |
| Guests   |        10     |        10%     |


 

## Main Function (main()):

- The main() function must only call methods and move data between them.

- **Your main() should:**
Call manage_capacity() to handle registration.
After registration, call greet_participant() to display custom greetings.
Call send_thank_you() to send follow-up thank-you messages.
Call collect_event_data() to analyze attendance.
Finally, call display_registration_stats() to print out a summary.
 

### Code Organization:

**Each function/method must have a specific task and handle its own logic.**

The main program logic must be broken down into these discrete methods, ensuring each method is focused on one aspect of the event management process.

```python
def register_participant():

    # Handle event registration logic

    pass


def validate_role(role):

    # Validate the role and prompt for re-entry if invalid

    pass

 

def check_guest_list(name):

    # Check if the guest is on the allowed list

    pass

 

def manage_capacity():

    # Manage registrations and stop once capacity is reached

    pass

 

def greet_participant(name):

    # Provide custom greetings based on the participant's name

    pass

 

def send_thank_you(name, role, registration_days):

    # Send thank-you message based on conditions

    pass

 

def collect_event_data():

    # Collect and analyze attendance data

    pass

 

def display_registration_stats(student_count, faculty_count, guest_count):

    # Display final registration statistics

    pass

 

def main():

    # Call methods and move data between them

    manage_capacity()

    # Other function calls go here

    pass

 

if __name__ == "__main__":

    main()
```
 

## Submission Instructions:

- Submit your Python script (.py file) with all parts implemented.
Ensure that your code is modular, with all business logic inside methods.
Include comments explaining each method's purpose and how the logic works.
Submit sample input/output demonstrating the program's functionality.