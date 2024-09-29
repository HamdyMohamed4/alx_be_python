from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date  # Return the formatted future date

def main():
    # Display current date and time
    display_current_datetime()

    # Prompt the user to input the number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = calculate_future_date(days)  # Store the returned future date
        print(f"Future date: {future_date}")  # Print the future date
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()

