def FandC():
    while True:
        PROMPT = "Enter:\n1 to convert Fahrenheit to Celsius,\n2 to convert Celsius to Fahrenheit,\nor q to quit: "
        response = input(PROMPT)

        if response == "1":
            F = float(input("Enter a Fahrenheit Degree for converting to a Celsius Degree: "))
            C = (F - 32) * (5 / 9)
            print(f"{F}°F is equal to {C:.2f}°C\n")

        elif response == "2":
            C = float(input("Enter a Celsius Degree for converting to a Fahrenheit Degree: "))
            F = C * (9 / 5) + 32
            print(f"{C}°C is equal to {F:.2f}°F\n")

        elif response.lower() == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please enter 1, 2, or q.\n")


# Call the function
print()
FandC()


