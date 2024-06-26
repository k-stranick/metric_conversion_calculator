#########################################################
#Author : Kyle Stranick                                 #
#Class : ITN160                                         #
#Class Section : 401                                    #
#Date : 9/12/2023 finished 9/                           #
#Assignment : Assignment 3 - Metric Conversion Program  #
#Version : 1.0                                          #
#########################################################

###################
#Syntax References:
###################
#Use of elif function was learned from Pluralsight.com \/\/\/
#https://app.pluralsight.com/course-player?clipId=36740e83-4142-4b22-8df0-a8cbfb23897b
#Use of try/except block\/\/\/
#Cannon, Jason. (2016). Python Succinctly. p. 87, Syncfusion Inc.
#Gupta, Anubhav. Slither into Python. (2021?) p.135 chapter 14.3
##############
# Patch Notes:
##############
#first error 1.01: input was incorrect for the initial kg variable: fixed to correct string to include floats
#second error 1.02: invalid syntax for my print function. Changed format to correct string
#third error 1.03: elif syntax was incorrect due to incorrect indentation. Reformatted script with correct indentation
#fourth error 1.04: invalid selection error. could not register non-variables i.e. letters, special characters (cont.)
#(cont.) added try,except block to code to test for errors,  raise ValueError to else clause to the execute if a wrong
#(cont.) value is entered. <-go back and re-write
def main():
    # Display the menu
    print("\nMetric Conversion Program")
    print("\nPlease select the conversion you would like to do:\n")
    print("1: Kilograms to Pounds")
    print("2: Pounds to Kilograms")
    print("3: Liters to Gallons")
    print("4: Gallons to Liters")
    print("5: Exit\n")

    #tests for
    try:
        selection = int(input("Selection (1-5): "))

        # elif used in if statement for readablility
        if selection == 1:
            kg = float(input("\nEnter Value in Kilograms: "))
            lbs = kg * 2.2046
            print(f"\n{kg} kilograms is equal to {lbs:.2f} pounds.")

        elif selection == 2:
            lbs = float(input("\nEnter Value in Pounds: "))
            kg = lbs / 2.2046
            print(f"\n{lbs} pounds is equal to {kg:.2f} kilograms.")

        elif selection == 3:
            liter = float(input("\nEnter Value in Liters: "))
            gal = liter / 3.785412
            print(f"\n{liter} Liters is equal to {gal:.2f} Gallons.")

        elif selection == 4:
            gal = float(input("\nEnter Value in Gallons: "))
            liter = gal * 3.785412
            print(f"\n{liter:.2f} Gallons is equal to {gal:.2f} Liters.")

        elif selection == 5:
            print("\nGoodBye!")

        else:
            raise ValueError

    except ValueError:
        print("\nYou have not typed a valid selection, please run the program again.")


if __name__ == "__main__":
    main()
