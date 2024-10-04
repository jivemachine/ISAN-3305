import global_variables as gv
#import numpy as np # convert arrays into multidimensional arrays for attendee data


def register_participant():

    user_name = str(input("Enter user name: "))
    role = str(input("What is your role: (student, faculty, guest): "))
    days = int(input("How many days until the event: "))
    
    valid_role = validate_role(role)
    on_guest_list = check_guest_list(user_name)
    
    # validation rules
    while valid_role == False:
        print("Invalid registration attempt, either role is not valid or user is not on guest list.")
        role = str(input("What is your role: (student, faculty, guest): "))
        
    if role == "guest":
        while role == "guest" and  on_guest_list == False:
            print("Invalid registration attempt, either role is not valid or user is not on guest list.")
            user_name = str(input("Enter user name: "))
            role = str(input("What is your role: (student, faculty, guest): "))
            days = int(input("How many days until the event: "))
            valid_role = validate_role(role)
            on_guest_list = check_guest_list(user_name)

    
    if (valid_role and role != "guest"):
        if gv.number_of_registrants < gv.MAX_OCCUPANCY:
            gv.number_of_registrants += 1
            print("Registration successful!")
            return user_name, role, days
        else: 
            print("We have reached max occupancy for the event. Try again next year!")
    elif (valid_role and role == "guest" and on_guest_list):
        gv.number_of_registrants += 1
        print("Registration successful!")
        return user_name, role, days
 


def validate_role(role):
    
    # cleaning role string
    role = role.lower().strip()
    
    # array of approved roles
    roles = ["student", "faculty", "guest"]
    
    if role in roles:
        if role == "student":
            gv.students += 1
        elif role == "faculty":
            gv.faculty += 1
        else:
            gv.guests += 1
          
        # return true if role is valid    
        return True
    
    else:
        # return false if invalid role
        return False

 

def check_guest_list(name):

    #global guest_list
    name = name.lower()
    
    # check is name is on global guest_list array
    if name in gv.guest_list:
        return True
    else:
        return False

 

def manage_capacity():

    
    # while loop registers users 
    # converts their data to 4 separate arrays
    # 3 for indivudual data analysis for each value and one that is a master lsit of all attendeeas
    while gv.number_of_registrants < gv.MAX_OCCUPANCY:
        name, role, days = register_participant()
        gv.attendees.append(name)
        gv.attendee_roles.append(role)
        gv.attendee_days.append(days)
        gv.attendee_data.append([name, role, days])
    
    # once loop is done
    # output high level registration report
    if (gv.students / gv.MAX_OCCUPANCY) >= 0.75:
        print("This event is student-heavy")
    elif (gv.faculty / gv.MAX_OCCUPANCY) >= .50:
        print("Faculty are showing strong interest")
    elif gv.guests >= 10:
        print("Expect additional guest services.")
         

 

def greet_participant(name):

    # Provides custom greetings based on the participant's role in the event
    # if users name is in the global keynote_speakers array
    if name in gv.keynote_speakers:
        print(f"Hello {name}! We're excited for your presentation this evening.")
        
    # if users name is in the global chairpersons array
    elif name in gv.chairpersons:
        print(f"Hello Chairperson {name}, we're honored to seat you this evening!")
    else:
        print(f"Hello {name}, welcome to the event!")

 
# function sends thank you notes to users whose names are in the global keynote speakers array
# or to students and faculty members who registered within 8 or more days of the event
# guests who are not chairpersons or keynote speakers recieve no thank you msg
def send_thank_you(name, role, registration_days):


    if name in gv.keynote_speakers:
        print(f"Thank you {name} presenting at our event! You were amazing!")
    elif role == "faculty" or role == "student":
        if registration_days > 7:
            print(f"Thank you {name} for attending our event! We sent you an email with a feedback form to complete at your leisure.")
        else: 
            print(f"Thank you {name} for attending our event! Follow our events page for updates.") 
    else:
        return True

 
# function prokmpts user for how long theyve been at the event to analyze 
# how long attendees stayed at venue
# then outputs values
def collect_event_data():

    
    # data collection
    user_time = float(input("How long did you stay at the event? (enter whole number or decimal)"))
    
    # append new time to times array
    gv.times.append(user_time)
    
    # get output variables
    total_time = 0
    for time in gv.times:
        total_time = total_time + time
        
    
    avg_time = total_time / len(gv.times)
    
    max_time = max(gv.times)
    
    print(f"Total time for all attandees: {total_time}\n Avg Time per attendee: {avg_time}\n Max time spent by single attendee {max_time}")

 

# function displays statistics on spread of students to faculty to guests that
# attended the event and gives a % of each group in a table
def display_registration_stats(student_count, faculty_count, guest_count):
    total_attendance = student_count + faculty_count + guest_count
    
    print("| Category | Registrants | Percentage |")
    print("| -------- | ----------- | ---------- |")
    print(f"| Students | {student_count} | {student_count/total_attendance} |")
    print(f"| Faculty | {faculty_count} | {faculty_count/total_attendance} |")
    print(f"| Guests | {guest_count} | {guest_count/total_attendance} |")
    

 
# def convert_to_key_val_pair(array1, array2):
#     new_arr = {} # dictionary bcuz wtf python
    
#     for key in array1:
#         for val in array2:
#             new_arr[key] = val
#             array2.remove(val) 
#             break
            
#     return new_arr      

def main():
    
    # Initialize global variables to be used between methods
    gv.init_globals()

    #  validate registration of users, until event reaches maxx occupancy
    #  tracks spread of students to faculty to guests ratio
    #  adds each successfully registered user to attendees array & their role into the attendee role array
    #  outputs a high level opinionated report of the spread of attendees for the event
    manage_capacity()
    
    # greet each attendee and send thank you
    # then collect data from each attendee
    for user_profile in gv.attendee_data:
        greet_participant(user_profile[0])
        send_thank_you(user_profile[0], user_profile[1], user_profile[2])
        collect_event_data()
        
    # function displays registration data among all attendees
    display_registration_stats(gv.students, gv.faculty, gv.guests)

 

if __name__ == "__main__":
    main()