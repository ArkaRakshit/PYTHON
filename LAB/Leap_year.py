# Program to check if a given year is a leap year
year = int(input("Enter a year: "))

if year > 0:  
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print("Please enter a valid positive year.")
