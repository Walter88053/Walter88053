def CtoF(C):
    F = C * (9/5) + 32
    return F


# Take input from the user and convert it to float
print()
C = float(input("Enter a Celsius Degree for converting to a Fahrenheit Degree: "))

# Call the function and print the result
F = CtoF(C)
print(f"{C}°C is equal to {F:.2f}°F")

