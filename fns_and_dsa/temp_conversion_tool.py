# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the conversion factor."""
    return (celsius * 9/5) + 32

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))  # Prompt for temperature
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  # Prompt for unit

        if unit == 'F':
            celsius_temp = convert_to_celsius(temperature)  # Convert to Celsius
            print(f"{temperature}°F is {celsius_temp}°C")  # Display result
        elif unit == 'C':
            fahrenheit_temp = convert_to_fahrenheit(temperature)  # Convert to Fahrenheit
            print(f"{temperature}°C is {fahrenheit_temp}°F")  # Display result
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")  # Handle invalid unit

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")  # Handle invalid temperature input

if __name__ == "__main__":
    main()


