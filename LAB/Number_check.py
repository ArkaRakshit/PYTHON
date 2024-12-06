# Program to check if a number is positive, negative, or zero

def check_number():
    try:
        # Get input from the user
        num = float(input("Enter a number: "))

        # Check if the number is positive, negative, or zero
        if num > 0:
            print("The number is positive.")
        elif num < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Run the function
check_number()
