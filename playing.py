import difflib

def is_close_answer(user_answer, correct_answer, threshold=0.7):
    ratio = difflib.SequenceMatcher(None, user_answer.lower(), correct_answer.lower()).ratio()
    return ratio >= threshold

print(f"Welcome to our quiz game 8th July 2024")

playing = input('Do you want to join us in the game?: ')
if playing.lower() != 'yes':
    quit()
else:
    print(f"Okay! Let's play then :)")
    score = 0

    answer = input('Define the function of the print() function?: ').lower()
    if is_close_answer(answer, 'output a text or other data to the console'):
        print('Correct. Awesome!')
        score += 1
    else:
        print('Incorrect. Try again!')
        quit()
    
    answer = input('What is console in python?: ').lower()
    if is_close_answer(answer, 'a command line interpreter that takes input from the use, interprets it and gives the required output'):
        print('Correct, You are amazing!')
        score += 1
    else:
        print('Incorrect try again!')
        quit()

    answer = input("Define the function of Import statement?: ").lower()
    if is_close_answer(answer, 'Loads a module or specific components from a module into the current namespace'):
        print('Bravo!')
        score += 1
    else:
        print('null and void')
        quit()

    answer = input("Define the function of Assignment statemnts?: ").lower()
    if is_close_answer(answer, 'Assign values to variables'):
        print('You got it right!')
        score += 1
    else:
        print('you got it wrong!')
        quit()

    answer = input("What is the function of if stament in python programming?: ").lower()
    if is_close_answer(answer, 'to execute both the true part and false part of a given condition'):
        print('You are great!')
        score += 1
    else:
        print('Not yet!')
        quit()

    answer = input('Define the function of else statement in programming?: ').lower()
    if is_close_answer(answer, 'to specify what to do if the condition is false'):
        print('Beautiful!')
        score += 1
    else:
        print('Wrong!')
        quit()

    answer = input('Define the function of expression statement in programming?: ').lower()
    if is_close_answer(answer, 'to evaluate expression'):
        print('You are great!')
        score += 1
    else:
        print('Wrong!')

    answer = input('Define the function of else statement in programming?: ').lower()
    if is_close_answer(answer,'to specify what to do if the condition is false'):
        print('You are great!')
        score += 1
    else:
        print('You are wrong!')
        
    answer = input('Define the function of conditional statement in programming?: ').lower()
    if is_close_answer(answer, 'to execute code based on condition'):
        print('You made it :)!')
        score += 1
    else:
        print('Try again!')

    answer = input('Define the function of Looping statement in programming?: ').lower()
    if is_close_answer(answer, 'to repeat codes multiple times'):
        print('You are great!')
        score += 1
    else:
        print('Wrong')

    answer = input('Define the function defination statement in programming?: ').lower()
    if is_close_answer(answer, 'to define reusable functions'):
        print('You are great!')
        score += 1
    else:
        print('Try again!')
    
    answer = input('Define the function of Pass statement in programming?: ').lower()
    if is_close_answer(answer, 'placeholder for future codes'):
        print('You are great!')
        score += 1
    else:
        print('Try again!')

    answer = input('Define the function of Break and Continue statement in programming?: ').lower()
    if is_close_answer(answer, 'placeholder for future codes'):
        print('You are great!')
        score += 1
    else:
        print('Try again!')

    answer = input('Define the function of Del statement in programming?: ').lower()
    if is_close_answer(answer, 'to delete objects'):
        print('You are great!')
        score += 1
    else:
        print('Try again!')

    answer = input('Define the function of Global and Nonlocal statement in programming?: ').lower()
    if is_close_answer(answer, 'to modify variable scopes'):
        print('You are great!')
        score += 1
    else:
        print('Try again!')

    answer = input('Define the function of Assert statement in programming?: ').lower()
    if is_close_answer(answer, 'Debugging aid'):
        print('You are great!')
        score += 1
    else:
        print('Try again!')

    answer = input('Define the function of With statement in programming?: ').lower()
    if is_close_answer(answer, 'to simplify exception handling'):
        print('You are great!')
        score += 1
    else:
        print('Try again!')

    print("You got "+ str(score) + " questions correct!")
    print("You got "+ str((score / 17) * 100) + "%.")

    if score == 17:
        print("Congradulations, You won!")
    else:
        print('Failed try again. You have to attain 100% for you to win!')
