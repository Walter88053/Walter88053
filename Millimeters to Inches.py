def MMtoIn(MM):
    In = .03937007874015748 * MM    # Convert millimeters to inches
    return In


# Take input from the user and convert it to float
print()
MM = float(input("Enter a length in millimeters for converting to inches: "))

# Call the function and print the result
In = MMtoIn(MM)
print(f"{MM} millimeters is equal to {In:.8f} inches")

