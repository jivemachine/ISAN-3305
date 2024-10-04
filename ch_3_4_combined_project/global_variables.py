#import numpy as np

def init_globals():
    ## init globals
    global number_of_registrants 
    global MAX_OCCUPANCY 
    global students 
    global faculty 
    global guests
    global times 
    global attendee_data
    global guest_list 
    global keynote_speakers
    global chairpersons
    global attendees
    global attendee_roles
    global attendee_days
        
    ## set global vals
    number_of_registrants = 0
    MAX_OCCUPANCY = 2
    students = 0
    faculty = 0
    guests = 0
    times = []
    attendee_data = []
    guest_list = ["henry cavil", "darth vader", "george washington", "zach kelley", "king charles", "zendaya", "dennis rodman", "bill clinton", "george hw bush", "barney rubble"]
    keynote_speakers = ["king charles", "zendaya", "dennis rodman"]
    chairpersons = ["bill clinton", "george hw bush", "barney rubble"]
    attendees = []
    attendee_roles = []
    attendee_days = []
    #attendee_roles_key_value_pair = {}

