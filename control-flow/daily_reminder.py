# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Initialize reminder message
reminder_message = ""

# Process the task based on priority using a Match Case statement
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder_message += " that requires immediate attention today!"
        else:
            reminder_message += "."
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder_message += " please try to complete it soon!"
        else:
            reminder_message += ". You can address it when convenient."
    case "low":
        reminder_message = f"'{task}' is a low priority task."
        if time_bound == "yes":
            reminder_message += " However, it requires immediate attention today!"
        else:
            reminder_message += " Consider completing it when you have free time."
    case _:
        reminder_message = "Invalid priority level. Please enter 'high', 'medium', or 'low'."

# Print the customized reminder
print(reminder_message)


