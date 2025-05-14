def FttoCM(Ft):
    CM = Ft / .0328083989501312     # Convert feet to centimeters
    return CM


# Take input from the user and convert it to float
print()
Ft = float(input("Enter a length in feet for converting to centimeters: "))

# Call the function and print the result
CM = FttoCM(Ft)
print(f"{Ft} feet is equal to {CM:.8f} centimeters")

