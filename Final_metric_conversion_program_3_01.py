#########################################################
#Author : Kyle Stranick                                 #
#Class : ITN160                                         #
#Class Section : 401                                    #
#Date : 9/12/2023 finished 9/14/23                      #
#Assignment : Assignment 3 - Metric Conversion Program  #
#Version : 3.01                                         #
#########################################################

###################
#Syntax References:
###################
#https://app.pluralsight.com/course-player?clipId=36740e83-4142-4b22-8df0-a8cbfb23897b
#https://app.pluralsight.com/course-player?clipId=09158c21-9842-453d-9d03-51c2249b61ea
#https://stackoverflow.com/questions/32861481/python3-creating-error-for-input-of-negative
#Cannon, Jason. (2016). Python Succinctly. p. 87, Syncfusion Inc.
#Gupta, Anubhav. Slither into Python. (2021?) p.135 chapter 14.3
##############
# Version Notes:
##############
#Version 1.01: input was incorrect for the initial kg variable: fixed to correct string to include floats
#Version 1.02: invalid syntax for my print function. Changed format to correct string
#Version 1.03: elif syntax was incorrect due to incorrect indentation. Reformatted script with correct indentation
#Version 1.04: invalid selection error. could not register non-variables inputs i.e. letters, special characters (cont.)
#added try,except block to code to test for errors,  raise ValueError to else clause to the execute if a wrong
#value is entered.
#Version 2.01: implementation of while loop to let program restart instead of manual restart after each selection
#Version 3.01: Implementation of while loops within each conversion if block to prompt user for the correct value
#Version 3.02: added if/else condition statement to check if user input is positive
def main():
    # Displays the conversion menu
    print('\nMetric Conversion Program')
    print('\nPlease select the conversion you would like to do:\n')
    print('1: Kilograms to Pounds')
    print('2: Pounds to Kilograms')
    print('3: Liters to Gallons')
    print('4: Gallons to Liters')
    print('5: Exit\n')

    # Main loop to keep asking for user's selection
    while True:

        try:
            # Get user's selection
            selection = int(input("Selection (1-5): "))

            # Kilograms to Pounds conversion
            if selection == 1:
                # Second loop to prompt user for valid number input
                while True:
                    try:
                        # Get kilograms value from the user
                        kg = float(input("\nEnter Value in Kilograms: "))

                        # Checks if entered value is positive is also condition statement
                        if kg <= 0:
                            print("\nEnter a positive Number.")
                        else:
                            # Conversion calculation
                            lbs = kg * 2.2046
                            print(f"\n{kg} kilograms is equal to {lbs:.2f} pounds.\n")
                            break
                    except ValueError:
                        #Error message if the input is not a valid number
                        print("\nYou can only enter integers or decimals try again.")

            # Gallons to Liters conversion
            elif selection == 2:
                # Second loop to prompt user for valid number input
                while True:
                    try:
                        # Get gallons value from the user
                        lbs = float(input("\nEnter Value in Pounds: "))

                        # Checks if entered value is positive is also condition statement
                        if lbs <= 0:
                            print("\nEnter a positive number.")
                        else:
                            # Conversion calculation
                            kg = lbs / 2.2046
                            print(f"\n{lbs} pounds is equal to {kg:.2f} kilograms.\n")
                            break
                    except ValueError:
                        # Error message if the input is not a valid number
                        print("\nYou can only enter integers or decimals try again.")

            elif selection == 3:
                # Second loop to prompt user for valid number input
                while True:
                    try:
                        liter = float(input("\nEnter Value in Liters: "))

                        # Checks if entered value is positive is also condition statement
                        if liter <= 0:
                            print("\nEnter a positive number.")
                        else:
                            # Conversion calculation
                            gal = liter / 3.785412
                            print(f"\n{liter} Liters is equal to {gal:.2f} Gallons.\n")
                            break
                    except ValueError:
                        # Error message if the input is not a valid number
                        print("\nYou can only enter integers or decimals try again.")

            elif selection == 4:
                # Second loop to prompt user for valid number input
                while True:
                    try:
                        gal = float(input("\nEnter Value in Gallons: "))

                        # Checks if entered value is positive is also condition statement
                        if gal <= 0:
                            print("\nEnter a positive number.")
                        else:
                            # Conversion calculation
                            liter = gal * 3.785412
                            print(f"\n{liter:.2f} Gallons is equal to {gal:.2f} Liters.\n")
                            break

                    except ValueError:
                        # Error message if the input is not a valid number
                        print("\nYou can only enter integers or decimals try again.")

            # Option to exit the program
            elif selection == 5:
                print("\nGoodBye!")
                break

            else:
                # raise an error if user's selection is not within 1-5
                raise ValueError

        except ValueError:
            # Error message for invalid selection
            print("\nYou have not typed a valid selection, please enter (1-5).\n")


# ensures that the main function is called only when the script is executed directly
if __name__ == '__main__':
    main()
