print(f"Welcome to our quiz game 8th July 2024")

playing = input('Do you want to join us in the game?: ')
if playing.lower() != 'yes':
    quit()
else:
    print(f"Okay! Let's play then :)")
    score = 0

    answer = input('Define CPU?: ')
    if answer.lower() == 'central processing unit':
        print('Correct. You are the best!')
        score += 1
    else:
        print('Incorrect. Do not give up try again i trust you are able to get it right!')
    
    answer = input('Define GPU?: ')
    if answer.lower() == 'graphics processing unit':
        print('Correct, You are amazing!')
        score += 1
    else:
        print('Incorrect try again!')

    answer = input("Define RAM?: ")
    if answer.upper() == 'RANDOM ACCESS MEMORY':
        print('Bravo!')
        score += 1
    else:
        print('null and void')

    answer = input("What is the defination of SPU?: ")
    if answer.lower() == 'spark prevention unit':
        print('You got it right!')
        score += 1
    else:
        print('Wrong, do your best and try again. You will be there soon!')

    print("You got "+ str(score) + " questions correct!")
    print("You got "+ str((score / 4) * 100) + "%.")

    if score == 4:
        print("Congradulations, You won!")
    else:
        print('Failed try again. You have to attain 100% for you to win!')
