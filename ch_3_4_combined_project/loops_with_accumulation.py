def collect_event_data():
    # global array to collect times
    global times
    
    # data collection
    time = float(input("How long did you stay at the event? "))
    
    # append new time to times array
    times.append(time)
    
    # get output variables
    total_time = 0
    for time in times:
        total_time = total_time + time
        
    
    avg_time = total_time / len(times)
    
    max_time = times.max()
    
    return total_time, avg_time, max_time