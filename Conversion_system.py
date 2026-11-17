# UNIT CONVERSION SYSTEM
# Project: PS No. 9

def length_conversion():
    print("\n--- LENGTH CONVERSION ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Centimeters")
    print("4. Centimeters to Meters")

    choice = input("Enter your choice: ")

    try:
        value = float(input("Enter the value: "))

        if value < 0:
            print("Invalid value. Enter a positive number.")
        elif choice == "1":
            result = value * 0.621371
            print(f"{value} km = {result:.2f} miles")
        elif choice == "2":
            result = value / 0.621371
            print(f"{value} miles = {result:.2f} km")
        elif choice == "3":
            result = value * 100
            print(f"{value} m = {result:.2f} cm")
        elif choice == "4":
            result = value / 100
            print(f"{value} cm = {result:.2f} m")
        else:
            print("Invalid conversion choice.")

    except ValueError:
        print("Invalid value. Enter a number.")


def weight_conversion():
    print("\n--- WEIGHT CONVERSION ---")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")

    choice = input("Enter your choice: ")

    try:
        value = float(input("Enter the value: "))

        if value < 0:
            print("Invalid value. Enter a positive number.")
        elif choice == "1":
            result = value * 1000
            print(f"{value} kg = {result:.2f} g")
        elif choice == "2":
            result = value / 1000
            print(f"{value} g = {result:.2f} kg")
        elif choice == "3":
            result = value * 2.20462
            print(f"{value} kg = {result:.2f} pounds")
        elif choice == "4":
            result = value / 2.20462
            print(f"{value} pounds = {result:.2f} kg")
        else:
            print("Invalid conversion choice.")

    except ValueError:
        print("Invalid value. Enter a number.")


def temperature_conversion():
    print("\n--- TEMPERATURE CONVERSION ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter your choice: ")

    try:
        value = float(input("Enter the temperature: "))

        if choice == "1":
            result = (value * 9/5) + 32
            print(f"{value} C = {result:.2f} F")
        elif choice == "2":
            result = (value - 32) * 5/9
            print(f"{value} F = {result:.2f} C")
        elif choice == "3":
            result = value + 273.15
            print(f"{value} C = {result:.2f} K")
        elif choice == "4":
            if value < 0:
                print("Invalid Kelvin temperature.")
            else:
                result = value - 273.15
                print(f"{value} K = {result:.2f} C")
        else:
            print("Invalid conversion choice.")

    except ValueError:
        print("Invalid value. Enter a number.")


def time_conversion():
    print("\n--- TIME CONVERSION ---")
    print("1. Hours to Minutes")
    print("2. Minutes to Hours")
    print("3. Minutes to Seconds")
    print("4. Seconds to Minutes")

    choice = input("Enter your choice: ")

    try:
        value = float(input("Enter the value: "))

        if value < 0:
            print("Invalid value. Enter a positive number.")
        elif choice == "1":
            result = value * 60
            print(f"{value} hours = {result:.2f} minutes")
        elif choice == "2":
            result = value / 60
            print(f"{value} minutes = {result:.2f} hours")
        elif choice == "3":
            result = value * 60
            print(f"{value} minutes = {result:.2f} seconds")
        elif choice == "4":
            result = value / 60
            print(f"{value} seconds = {result:.2f} minutes")
        else:
            print("Invalid conversion choice.")

    except ValueError:
        print("Invalid value. Enter a number.")


def main():
    while True:
        print("\n================================")
        print("       UNIT CONVERSION SYSTEM")
        print("================================")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Temperature Conversion")
        print("4. Time Conversion")
        print("5. Exit")

        choice = input("Select a category (1-5): ")

        if choice == "1":
            length_conversion()
        elif choice == "2":
            weight_conversion()
        elif choice == "3":
            temperature_conversion()
        elif choice == "4":
            time_conversion()
        elif choice == "5":
            print("Thank you for using Unit Conversion System!")
            break
        else:
            print("Invalid choice. Select 1 to 4.")


# Run the program
if __name__ == "__main__":
    main()