def calculate_100_year_age():
    """Asks for name and age, then calculates the year the person will turn 100."""
    name = input("Enter your name: ")
    while True:
        try:
            age_str = input("Enter your age: ")
            age = int(age_str)
            if age <= 0:
                print("Please enter a valid age greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number for your age.")

    current_year = 2025  # Based on the current date
    years_to_100 = 100 - age
    year_at_100 = current_year + years_to_100

    print(f"{name} will be 100 years old in {year_at_100}.")

if __name__ == "__main__":
    calculate_100_year_age()