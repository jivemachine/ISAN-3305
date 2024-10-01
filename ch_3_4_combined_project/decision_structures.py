number_of_registrants = 0
MAX_OCCUPANCY = 100

def register_participant():
    # global variables used
    global number_of_registrants
    global MAX_OCCUPANCY
    
    user_name = str(input("Enter user name: "))
    role = str(input("What is your role: (student, faculty, guest)"))
    
    if number_of_registrants < MAX_OCCUPANCY:
        number_of_registrants += 1
        print("Registration successful!")
    else: 
        print("We have reached max occupancy for the event. Try again next year!")
        
        
def validate_role(role):
    # cleaning role string
    role = role.lower().strip()
    
    # array of approved roles
    roles = ["student", "faculty", "guest"]
    
    if role in roles:
        return True
    else:
        return False
        
        
def check_guest_list(name):
    if name in guest_list:
        return True
    else:
        return False
    