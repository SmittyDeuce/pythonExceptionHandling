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

tempCheck()


# Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be converted to a number.

# Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.
# Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

def tempConversion():
    try:
        fahrenheit = input("What is the temperature in Fahrenheit? ")
        fahrenheit = int(fahrenheit)
        celcius = (fahrenheit - 32) * 5/9
        celcius = int(celcius)
        print(f"{fahrenheit} degrees F is {celcius} C")

        # except zerodivisionerror takes into the account 
        # if 0 will ever be the divisor  
    except ZeroDivisionError:
        print("It is impossible to divide by 0")
        #  not to confuse with stack overflow which can lead to Overflow error
        # OverflowError will occur if an input exceeds max val for numeric data 
    except OverflowError as e:
        print("Overflow error occurred: ", e)

tempConversion()


# Task 3: User Experience
# Implement an else block that prints the converted temperature in a user-friendly format.
# Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

def tempConversion():
    try:
        fahrenheit = input("What is the temperature in Fahrenheit? ")
        fahrenheit = int(fahrenheit)
        celcius = (fahrenheit - 32) * 5/9
        celcius = int(celcius)

        # except zerodivisionerror takes into the account 
        # if 0 will ever be the divisor  
    except ZeroDivisionError:
        print("It is impossible to divide by 0")
        #  not to confuse with stack overflow which can lead to Overflow error
        # OverflowError will occur if an input exceeds max val for numeric data 
    except OverflowError as e:
        print("Overflow error occurred: ", e)
    
    except ValueError:
        print("Please enter an Integer")

    else:
        print("The Temperature in Celcius is: ", celcius)


    # finally statements will always print no matter what
    finally:
        print("Thank you for using the Weather Forcast Application")

tempConversion()


# 2. The Recipe Ratio Adjuster
# Objective: The aim of this assignment is to create a program that adjusts the quantities of a recipe based on the number of servings, handling any type of arithmetic errors or user input exceptions.

# Task 1: Start
# Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.
# Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

def start():
    try:
        originalServings = input("How many servings does original call for?: " )
        personalizedServings = input("How many do you want to make?: " )
        originalServings = int(originalServings)
        personalizedServings = int(personalizedServings)

    except ValueError:
        print("Response must be a number")

start()


# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired servings by the original servings.
# Use a try block to catch any arithmetic errors that may occur during the calculation.

def quantity():
    try:
        originalServings = input("How many servings does original call for?: " )
        personalizedServings = input("How many do you want to make?: " )
        originalServings = int(originalServings)
        personalizedServings = int(personalizedServings)
        adjustedRecipe = personalizedServings / originalServings

    except ValueError:
        print("Response must be a number")
    
    except ZeroDivisionError:
        print("We can not divide a number by 0")

    except OverflowError as e:
        print("Error Overflow in outputs")


quantity()






# Task 3: Serving Success
# If the calculation is successful, display the adjusted recipe quantities to the user.
# Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.

def servingSuccess():
    try:
        originalServings = input("How many servings does original call for?: " )
        personalizedServings = input("How many do you want to make?: " )
        originalServings = int(originalServings)
        personalizedServings = int(personalizedServings)
        adjustedRecipe = personalizedServings / originalServings

    except ValueError:
        print("Response must be a number")
    
    except ZeroDivisionError:
        print("We can not divide a number by 0")

    except OverflowError as e:
        print("Error Overflow in outputs")

    else:
        print(f"for your personal request you will need {adjustedRecipe} serving(s)")

    finally:
        print("May you enjoy the meal you are to cook")

servingSuccess()