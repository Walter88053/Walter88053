def MtoFt(M):
    Ft = 3.28083989501312 * M     # Convert meters to feet
    In = 39.37007874015748 * M    # Convert meters to inches
    return Ft, In


# Take input from the user and convert it to float
print()
M = float(input("Enter a length in meters for converting to feet and also inches: "))

# Call the function and print the result
Ft, In = MtoFt(M)
print(f"{M} meters is equal to {Ft:.8f} feet or {In:.8f} inches")

