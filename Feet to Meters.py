def FttoM(Ft):
    M = Ft / 3.28083989501312     # Convert feet to meters
    return M


# Take input from the user and convert it to float
print()
Ft = float(input("Enter a length in feet for converting to meters: "))

# Call the function and print the result
M = FttoM(Ft)
print(f"{Ft} feet is equal to {M:.8f} meters")

