    control-flow/daily_reminder.py

# daily_reminder.py
# A program that gives a reminder for a single task using match-case, conditionals, and loops

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Handle time-bound with a while loop (just to reinforce loop usage)
while True:
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
        break
    elif time_bound == "no":
        reminder = "Note: " + reminder + ". Consider completing it when you have free time."
        break
    else:
        time_bound = input("Invalid input. Please type yes or no: ").lower()

# Print the final reminder
print("\nReminder:", reminder)
