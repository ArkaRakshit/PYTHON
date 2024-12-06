def check_voting_eligibility(age):
    """Function to check voting eligibility based on age."""
    if age < 0:
        print("Invalid age. Please enter a valid positive number.")
    elif age < 18:
        print("You are not eligible to vote. You must be 18 or older.")
    else:
        print("You are eligible to vote!")

# Get user input
try:
    age = int(input("Enter your age: "))
    check_voting_eligibility(age)
except ValueError:
    print("Invalid input. Please enter a valid number.")
