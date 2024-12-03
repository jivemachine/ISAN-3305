# Logic for project

## Requirements:

#### Topic:
- **Music:** guitar chords suggestor. (I wanna build a guitar chord recommendation system based on musical style and chords the user already has selected)
    -  I found a data set on kaggle that has artists, their songs chord progressions and the artists genre. I could use genre and chord progression (Chord progression in dataset is using the number system in dataset making them *key agnostic*) this for the project.


>Full disclosure, I graduated from a data science bootcamp called codeup in 2020 and have some amateur experience in machine learning with sklearn and some industry experience as an intern creating deep learning models using keras & tensorflow (This was in 2020 so I am rusty and behind on the times in terms of what is current). But, could be a fun project building a recommendation system even a lean weak-ass version of one that does not utilize ML'ing.

### Take user input:
- User inputs chords they are using ~~(Max 3 chords)~~ ~~(Max 2 chords)~~ (Max 1 chord) 
- Program asks what style they are writing the music for (Start with short list with genres like pop, and rock, and expand genres as I develop the program and feel confident in adding more content to the application)

### File Handling:
- load csv with data concerning genres used in the program *or-if* this is a big **or-if** if I decide to go the machine learning route I can accomplish this with data from [kaggle's contemporary song music data set](https://www.kaggle.com/datasets/danield2255/contemporary-song-music-data). Also, consider other potential datasets.

### Data parsing & manipulation
- I would have to add a sort of data analytics component to the project to accomplish this, even if rudimentary. Maybe utilizing **matplotlib**
    - (Parse string data into an array, perform basic operations on the array, cacl min & max, calc total, sort array)

### Dictionary usage:
- use **pandas** for data manipulation. (Dataframes are just Dictionaries with extra features ;D)

### Dynamic Menu
- I could either try to build a command line interface for this or build a little application using flask or django & deploy it on railway, vercel, etc...

### validation:
- if using command line interface validate user input
- using a web page I don't think there would be any need for validation as the application would be a SPA with no database or user log in needed.

### GUI Interaction:
- If using CLI, I could use tkinter's messagebox for this. (Otherwise I would have to use JS or a styling framework like twitter bootstrap if finishing this project using something like django unless there is a python styling library that I am unaware of)
    - Add pop up messages (modals) showing user's selected option from the menu.

### Submission guidlines:
- program has to be python
- submit work as a single .py file
- include sample file for testing program
- ensure graceful error handling

#### Evaluate Criteria:
Project will be assessed on:

**Functionality**
- Does the program include all required features
- Is the data handled correctly handled and processed

**Code Quality**
- Is the code easy to follow?
- Are variables and functions named appropriatly? 

**Error Handling**
- Does the program handle invalid inputs or errors *gracefully?*

**UI/UX**
- Is the menu easy to navigate?
- Does the popup provide clear feedback?





