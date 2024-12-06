# Program to check if a number is even or odd

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Taking input from the user
try:
    user_input = int(input("Enter a number: "))
    result = check_even_odd(user_input)
    print(result)
except ValueError:
    print("Please enter a valid integer.")
