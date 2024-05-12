import sys
import Tasks as TasksObj
import Timer as timerObj
import threading

"""
This is the main file of the timer/task manager program.
This file will handle user input.
"""


def main():
    print("------------------------")
    print("|Timer and task manager|")
    print("------------------------")

    while True:
        try:
            Main_menu()

            mainMenuIn = int(input("Your choice: "))

            match mainMenuIn:
                case 1:
                    task_Manager_Menu_Input()
                case 2:
                    timer_Menu_Input()
                case 3:
                    break
                case _:
                    print("Your input is out of bounds. Please try again.")
                    
        except ValueError:
            print("")
            print("You input the wrong data type. You are supposed to input an integer.")
            print("")
            
    sys.exit()

# The three methods below print menu options for the user.
def task_Manager_Menu():
    print("1) Create tasks")
    print("2) Remove tasks")
    print("3) Print Tasks")
    print("4) Back")

def timer_Menu():
    print("1) Set time?")
    print("2) Start timing")
    print("3) Back")

def Main_menu():
    print("1) Task Manager")
    print("2) Timer")
    print("3) Exit")

# Tasks task_Manager_Menu_Input handles user input for tasks management.
def task_Manager_Menu_Input():
    
    while True:
        try:
            task_Manager_Menu()

            taskManagerInput = int(input("Your choice: "))

            match taskManagerInput:
                case 1:
                    taskDetails = input("Input your task: ")
                    TasksObj.TasksObj().addToList(taskDetails)

                case 2:
                    if TasksObj.TasksObj().getTaskCount() == 0:
                        print("There are no tasks to remove.")
                    else:
                        index = int(input("Input index of a task to remove: "))
                        TasksObj.TasksObj().removeList(index)

                case 3:
                    TasksObj.TasksObj().printList()

                case 4:
                    break
                case _:
                    print("Your input is out of bounds. Please try again.")

        except ValueError:
            print("")
            print("You input the wrong data type. You are supposed to input an integer.")
            print("")

def timer_Menu_Input():

    while True:
        try:
            timer_Menu()

            timerMenuIn = int(input("Your choice: "))

            match timerMenuIn:
                case 1:
                    timerObj.timerObj().checkIfFormatCorrect()
                case 2:
                    if timerObj.timerObj().getTime():
                        print("You haven't set a time limit yet. Please do that first.")
                    else:
                        # Thread call is necessary so the timer can run in the background.
                        timerThread = threading.Thread(target = timerObj.startTimer())
                        timerThread.start()
                case 3:
                    main()
                case _:
                    print("Your input is out of bounds. Please try again.")
        except ValueError:
            print("")
            print("You input the wrong data type. You are supposed to input an integer.")
            print("")

if __name__ == "__main__":
    main()
