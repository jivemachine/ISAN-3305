import global_variables
import register_participant from decision_structures

def manage_capacity():
    # global variable
    global MAX_OCCUPANCY
    global number_of_registrants
    global students
    global faculty
    global guests
    
    while number_of_registrants < MAX_OCCUPANCY:
        register_participant()
      
    # registration report
    if (students / MAX_OCCUPANCY) >= 0.75:
        print("This event is student-heavy")
    elif (faculty / MAX_OCCUPANCY) >= .50:
        print("Faculty are showing strong interest")
    elif guests >= 10:
        print("Expect additional guest services.")
        
        
    
    