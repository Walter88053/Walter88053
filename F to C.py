def FtoC(F):
    C = (F - 32) * (5/9)
    return C


# Take input from the user and convert it to float
print()
F = float(input("Enter a Fahrenheit Degree for converting to a Celsius Degree: "))

# Call the function and print the result
C = FtoC(F)
print(f"{F}°F is equal to {C:.2f}°C")

