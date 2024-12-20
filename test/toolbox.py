# file containing useful functions and methods so 
# I don't have to remember everything from scratch 
# during tomorrows test

# IMPORTS
import random as r
import os
import pandas as pd
import numpy as np
import turtle as t
import uuid


# GLOBAL VARIABLES
FILE = 'file.txt'


def overwrite_txt_file(dictionary: dict, file = FILE) -> None:
    # overwrite file contents
    with open(file, "w") as f:
        # iterate through dictionary
        for row in dictionary:
            # write data to file 
            f.write(f"{row},{dictionary[row]}\n")
        return None

# random 
def random_shit():
    # generate random integer
    random_num = r.randint(0, 100)
    
    # generate random float
    random_float = r.random()
    
    # use random seed example
    r.seed(42)
    
    # random sample to choose any random value in array
    random_array = np.random.rand(10)
    r.choice(random_array) # choose a random element from this array
    
    for i in random_array:
        r.choice(random_array)
        
def arrays_n_dict():
    data = {}
    
    # adding data to dictionary
    for i in range(5):
        data[i] = random_string(4)
        # outputs: {0: "A32D", 1: "FE5G"}
    
    # convert current string value into its own dictionary
    for x in data:
        data[x] = {data[x]}
        # outputs: { 0: {"DEF0"} }
            
        
        
    print(data)
    
def random_string(string_length=10):
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.    

# sorting using lambdas and dictionary
def sort_and_display():
    # load data from file
    data = {0: "data0", 1: "data1"}
    
    # sort in descending order
    sorted_dict = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    
    # display dictionary
    print("Current Grades:")
    for student in sorted_dict:
        print(f"{student}: {sorted_dict[student]}")
