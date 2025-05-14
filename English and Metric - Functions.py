# Conversion functions
def mm_to_inch(value):
    return value * 0.03937007874015748

def cm_to_inch(value):
    return value * 0.3937007874015748

def inch_to_mm(value):
    return value / 0.03937007874015748

def inch_to_cm(value):
    return value / 0.3937007874015748

def ft_to_cm(value):
    return value / 0.0328083989501312

def ft_to_m(value):
    return value / 3.28083989501312

def m_to_ft(value):
    return value * 3.28083989501312

def m_to_inch(value):
    return value * 39.37007874015748

# Main function with menu
def EandM():
    conversions = {
        "1": ("millimeters", "inches", mm_to_inch),
        "2": ("centimeters", "inches", cm_to_inch),
        "3": ("inches", "millimeters", inch_to_mm),
        "4": ("inches", "centimeters", inch_to_cm),
        "5": ("feet", "centimeters", ft_to_cm),
        "6": ("feet", "meters", ft_to_m),
        "7": ("meters", "feet", m_to_ft),
        "8": ("meters", "inches", m_to_inch)
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
            from_unit, to_unit, func = conversions[response]
            try:
                value = float(input(f"Enter a length in {from_unit} to convert to {to_unit}: "))
                result = func(value)
                print(f"{value} {from_unit} is equal to {result:.8f} {to_unit}\n")
            except ValueError:
                print("Invalid number. Please try again.\n")
        else:
            print("Invalid input. Please enter a number from 1 to 8, or 'q' to quit.\n")

# Run the function
EandM()
