def find_largest():
    print("Enter three numbers to find the largest:")
    try:
        # Taking inputs from the user
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = int(input("Enter the third number: "))

        # Finding the largest number
        largest = max(num1, num2, num3)

        print(f"The largest number among {num1}, {num2}, and {num3} is {largest}")
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the function
find_largest()
