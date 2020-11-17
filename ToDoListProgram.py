# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# CRoss,11.12.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open("ToDoList.txt", "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(f"{row['Task']}, {row['Priority']}")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Please enter a new task: ")  # Get task from user
        strTask = strTask.title()  # Format entry
        intPriority = int(input("Please enter priority: "))  # Get priority from user
        dicRow = {"Task": strTask, "Priority": intPriority}  # Add user input to dict
        lstTable.append(dicRow)  # Add new row to table
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strTask = input("Task to be removed: ")  # Determine what task the user wants to remove
        for row in lstTable:  # iterate over current entries to find task user entered
            if strTask.lower() in row["Task"].lower():  # if task in a row matches user input, remove row
                lstTable.remove(row)
        if strTask not in lstTable:
            print("Task not found, please enter task in list")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")  # open file in write mode
        for row in lstTable:  # iterate over entries in table to write to file
            objFile.write(f"{row['Task']},{row['Priority']}\n")  # write to file, format appropriately
        objFile.close()  # close file
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        strSave = input("Save any changes? [Y/N]: ")  # Check if the user needs to save
        if strSave.lower() == "y":  # If yes, save everything to the file then quit
            objFile = open("ToDoList.txt", "w")
            for row in lstTable:
                objFile.write(f"{row['Task']},{row['Priority']}\n")
            objFile.close()
            print("Changes saved!")
            break
        elif strSave.lower() == "n":  # If no, quit program
            break  # and Exit the program
