def CMtoIn(CM):
    In = .3937007874015748 * CM    # Convert centimeters to inches
    return In


# Take input from the user and convert it to float
print()
CM = float(input("Enter a length in centimeters for converting to inches: "))

# Call the function and print the result
In = CMtoIn(CM)
print(f"{CM} centimeters is equal to {In:.8f} inches")

