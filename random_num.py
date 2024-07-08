import random

def number_guesing_game():
    lower_number = 1
    upper_number = 1000000
    target_number = random.randint(lower_number, upper_number)
    attempts = 0

    while true:
        try:
            gues = int(input(f"gues a number betweeen {lower_number} and {upper_number}: "))
            if lower_number <= gues <= upper_number:
                attempt += 1
                if gues == target_number:
                    print(f"Conradulations! You guest the correct number ({target_number}) in {attempts} attempts.")
                    break
                elif gues < target_number:
                    print(f"Try a higher number.")
                else:
                    print("Try a lower number.")
                else:
                    print("Invalid input. Please a number with the specified range.")
        except Valueerror:
            print("Invalid input. Please enter a valid number.")

number_guesing_game()
