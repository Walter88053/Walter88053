def IntoMM(In):
    MM = In / .03937007874015748     # Convert inches to millimeters
    return MM


# Take input from the user and convert it to float
print()
In = float(input("Enter a length in inches for converting to millimeters: "))

# Call the function and print the result
MM = IntoMM(In)
print(f"{In} inches is equal to {MM:.8f} mill36imeters")

