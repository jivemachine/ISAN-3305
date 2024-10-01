def greet_participant(name):
    if name in keynote_speakers:
        print(f"Hello {name}! We're excited for your presentation this evening.")
    elif name in chairpersons:
        print(f"Hello Chairperson {name}, we're honored to seat you this evening!")
    else:
        print(f"Hello {name}, welcome to the event!")