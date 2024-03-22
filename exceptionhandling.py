# 1. Exceptional Weather Forecast
# Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

# Task 1: Start
# Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

def tempCheck():

    # using try in case a user tries to input a non integer
    try:
        temperature = input("What is temperature in Fahrenheit? ")
        temperature = int(temperature)
        print(f"Current Temperature {temperature} F")
    except ValueError:
        # code to print in event user input is not digit
        print("Please enter a numeric value ")

# tempCheck()


# Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be converted to a number.

# Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

def tempConversion():
    try:
        fahrenheit = input("What is the temperature in Fahrenheit? ")
        fahrenheit = int(fahrenheit)
        celcius = (fahrenheit - 32) * 5/9
        celcius = int(celcius)
        print(f"{fahrenheit} degrees F is {celcius} C")
    except ZeroDivisionError:
        print("It is impossible to divide by 0")

tempConversion()



# Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

# Task 3: User Experience
# Implement an else block that prints the converted temperature in a user-friendly format.

# Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

# 2. The Recipe Ratio Adjuster
# Objective: The aim of this assignment is to create a program that adjusts the quantities of a recipe based on the number of servings, handling any type of arithmetic errors or user input exceptions.

# Task 1: Start
# Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.

# Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired servings by the original servings.

# Use a try block to catch any arithmetic errors that may occur during the calculation.

# Task 3: Serving Success
# If the calculation is successful, display the adjusted recipe quantities to the user.

# Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.