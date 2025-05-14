def IntoCM(In):
    CM = In / .3937007874015748     # Convert inches to centimeters
    return CM


# Take input from the user and convert it to float
print()
In = float(input("Enter a length in inches for converting to centimeters: "))

# Call the function and print the result
CM = IntoCM(In)
print(f"{In} inches is equal to {CM:.8f} centimeters")

