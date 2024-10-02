def send_thank_you(name, role, registration_days):
    if role == "faculty" or role == "student":
        if registration_days > 7:
            print(f"Thank you {name} for registering! You will received an email with a feedback form after the event takes place.")
        else: 
            print(f"Thank you {name} for registering! Follow our events page for updates.")
    elif name in keynote_speakers:
        print(f"Thank you {name} for registering, we're excited to hear your presentation during the event!")
    else:
        break