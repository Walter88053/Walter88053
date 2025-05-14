def EandM():
    while True:
        PROMPT = ("Enter:\n1 to convert Millimeters to Inches,\n2 to convert Centimeters to Inches,\n3 to convert Inches to Millimeters,"
                  "\n4 to convert Inches to Centimeters,\n5 to convert Feet to Centimeters,\n6 to convert Feet to Meters,"
                  "\n7 to convert Meters to Feet,\n8 to convert Meters to Inches,\nor q to quit: ")
        response = input(PROMPT)

        if response == "1":
            # Take input from the user and convert it to float
            MM = float(input("Enter a length in millimeters for converting to inches: "))
            In = .03937007874015748 * MM  # Convert millimeters to inches
            print(f"{MM} millimeters is equal to {In:.8f} inches")

        if response == "2":
            # Take input from the user and convert it to float
            CM = float(input("Enter a length in centimeters for converting to inches: "))
            In = .3937007874015748 * CM  # Convert centimeters to inches
            print(f"{CM} centimeters is equal to {In:.8f} inches")

        if response == "3":
            # Take input from the user and convert it to float
            In = float(input("Enter a length in inches for converting to millimeters: "))
            MM = In / .03937007874015748  # Convert inches to centimeters
            print(f"{In} inches is equal to {MM:.8f} millimeters")

        if response == "4":
            # Take input from the user and convert it to float
            In = float(input("Enter a length in inches for converting to centimeters: "))
            CM = In / .3937007874015748  # Convert inches to centimeters
            print(f"{In} inches is equal to {CM:.8f} centimeters")

        if response == "5":
            # Take input from the user and convert it to float
            Ft = float(input("Enter a length in feet for converting to centimeters: "))
            CM = Ft / .0328083989501312  # Convert feet to centimeters
            print(f"{Ft} feet is equal to {CM:.8f} centimeters")

        if response == "6":
            # Take input from the user and convert it to float
            Ft = float(input("Enter a length in feet for converting to meters: "))
            M = Ft / 3.28083989501312  # Convert feet to meters
            print(f"{Ft} feet is equal to {M:.8f} meters")

        if response == "7":
            # Take input from the user and convert it to float
            M = float(input("Enter a length in meters for converting to feet: "))
            Ft = 3.28083989501312 * M  # Convert meters to feet
            print(f"{M} meters is equal to {Ft:.8f} feet")

        if response == "8":
            # Take input from the user and convert it to float
            M = float(input("Enter a length in meters for converting to Inches: "))
            In = 39.37007874015748 * M  # Convert meters to inches
            print(f"{M} meters is equal to {In:.8f} inches")

        elif response.lower() == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please enter 1, 2, or q.\n")


# Call the function and print the result
print()
EandM()


