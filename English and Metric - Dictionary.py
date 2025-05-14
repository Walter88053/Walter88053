def EandM():
    conversions = {
        "1": ("millimeters", "inches", 0.03937007874015748),
        "2": ("centimeters", "inches", 0.3937007874015748),
        "3": ("inches", "millimeters", 1 / 0.03937007874015748),
        "4": ("inches", "centimeters", 1 / 0.3937007874015748),
        "5": ("feet", "centimeters", 1 / 0.0328083989501312),
        "6": ("feet", "meters", 1 / 3.28083989501312),
        "7": ("meters", "feet", 3.28083989501312),
        "8": ("meters", "inches", 39.37007874015748)
    }

    prompt = (
        "Enter:\n"
        "1 to convert Millimeters to Inches,\n"
        "2 to convert Centimeters to Inches,\n"
        "3 to convert Inches to Millimeters,\n"
        "4 to convert Inches to Centimeters,\n"
        "5 to convert Feet to Centimeters,\n"
        "6 to convert Feet to Meters,\n"
        "7 to convert Meters to Feet,\n"
        "8 to convert Meters to Inches,\n"
        "or q to quit: "
    )

    while True:
        response = input(prompt).strip().lower()

        if response == "q":
            print("Goodbye!")
            break
        elif response in conversions:
            from_unit, to_unit, factor = conversions[response]
            try:
                value = float(input(f"Enter a length in {from_unit} to convert to {to_unit}: "))
                result = value * factor
                print(f"{value} {from_unit} is equal to {result:.8f} {to_unit}")
            except ValueError:
                print("Invalid number. Please try again.\n")
        else:
            print("Invalid input. Please enter a number from 1 to 8, or 'q' to quit.\n")

# Run it
EandM()
