# Task 1


def celsius_conv():
    while True:
        try:
            fahr = float(input("Enter the temperature in Fahrenheit: "))
            celsius = (fahr - 32) * 5/9
        except ValueError:
            print("Type the temperature in numeric form.")
        else: 
            print(f"{fahr} degrees Fahrenheit is {celsius:.2f} degrees Celsius")
        finally:
            choice = input("""Thank you for using the weather forecast app. 
Would you like to enter another temperature? Y/N: """).upper()

        if choice != "Y":
            break



celsius_conv()