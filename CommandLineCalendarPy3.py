"""
A basic calendar that the user will interact with from the command line. The user should be able to:

- View the calendar
- Add an event to the calendar
- Update an existing event
- Delete an existing event
- The program should behave in the following way:

1.) Print a welcome message to the user
2.) Prompt the user to view, add, update, or delete an event on the calendar
3.) Depending on the user's input: view, add, update, or delete an event on the calendar
4.) The program should never terminate unless the user decides to exit
"""

from time import sleep, strftime

print("Welcome to a very basic command line calendar app.")
user = input("Tell me your name! ")

calendar = {}


def welcome():
    print("Welcome " + user + ".")
    print("The calendar is now opening.")
    sleep(1)  # We use the sleep function to give the user some time to read the text.
    print("Today is: " + strftime("%A %B %d, %Y"))
    print("The time is now: " + strftime("%I:%M:%S"))
    sleep(1)
    print("What would you like to do?")


def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = input("A to Add, U to Update, V to View, X to Exit: ")
        user_choice = user_choice.upper()
        if user_choice == 'V':
            if len(calendar.keys()) < 1:
                print("The calendar is currently empty. There's nothing to view.")
            else:
                print(calendar)
        elif user_choice == "U":
            print("This is used for updating the name of events.")
            date = input("Which date do you want to update the event name to?: ")
            update = input("Enter the update: ")
            calendar[date] = update
            print("Update made successfully!")
            print(calendar)
        elif user_choice == "A":
            event = input("Enter the name of the event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
                print("Invalid entry. Make sure it's in the format of MM/DD/YYYY and that it's this year or later.")
                try_again = input("Try again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    print("Okay, exiting now.")
                    start = False
            else:
                calendar[date] = event
        elif user_choice == "X":
            start = False
        else:
            print("Sorry, you entered an invalid command. Exiting the program now.")
            start = False

start_calendar()
