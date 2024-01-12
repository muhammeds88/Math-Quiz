import random
import time

# Get user's name input
name = input('Enter your Name: ')

while True:
    def grade():
        # Evaluate and print the grade based on the number of correct answers
        if correct >= 8:
            print('Excellent! You got A grade.')
        elif 5 < correct < 8:
            print("Good! You got B grade.")
        elif 3 < correct < 5:
            print("Need Improvement! You got C grade.")
        elif correct <= 3:
            print('Very Bad! You got D grade.')


    # Constants for the math quiz
    SIGN = ['+', '-', '*']
    MIN_NUM = 1
    MAX_NUM = 10
    TOTAL_PROBLEMS = 10

    # Function to create a math problem
    def create_problem():
        left_num = random.randint(MIN_NUM, MAX_NUM)
        right_num = random.randint(MIN_NUM, MAX_NUM)
        operator = random.choice(SIGN)

        exprmnt = str(left_num) + ' ' + operator + ' ' + str(right_num)

        answer = eval(exprmnt)
        return exprmnt, answer

    # Variables to track correct and wrong answers
    wrong = 0
    correct = 0

    # Introduction for the sample test
    print('\nSample Test')
    print(f'Hello {name} welcome to Maths Test.\nYou have total 10 questions to be done in Sample Test.\n'
          f'----------------------------\nNumbers included = [1 - 10]\nSigns included = [+, -, *]\n'
          f'----------------------------\nThe time taken to complete the task will be shown')
    print("All the Best!")
    input('Press Enter to Start.')
    print('-------------------------')

    start_time = time.time()

    # Loop through total problems for the sample test
    for i in range(TOTAL_PROBLEMS):
        exprmnt, answer = create_problem()
        while True:
            guess = input('Problem #' + str(i + 1) + ' : ' + exprmnt + ' = ')
            if guess == str(answer):
                correct += 1
                break
            else:
                print("Wrong answer.")
                wrong += 1
                break

            i += 1

    finish_time = time.time()
    total_time = round(finish_time - start_time, 3)

    # Display results and grade for the sample test
    print(f'You got {correct} correct answers and {wrong} wrong answers')
    grade()

    print("You have finished in: ", total_time, 'seconds')

    # Ask if the user wants to continue to the next level
    again = input("\nDo you want to continue to the next level? (y or n) ")
    if again != 'y':
        quit()

    # Prompt the user to select the difficulty level
    mode = input("Enter 'e' for Easy\nEnter 'h' for Hard\n")

    if mode == 'e':
        def gradee():
            # Evaluate and print the grade for the Easy level
            if correct > 4:
                print('Excellent! You got A grade.')
            elif correct == 4:
                print("Good! You got B grade.")
            elif correct == 3:
                print("Need Improvement! You got C grade.")
            elif correct <= 2:
                print('Very Bad! You got D grade.')

        # Update constants for the Easy level
        MIN_NUM = 0
        MAX_NUM = 5
        SIGN = ['+', '-']
        TOTAL_PROBLEMS = 5

        # Reset variables for the Easy level
        wrong = 0
        correct = 0

        # Introduction for the Easy level
        print('**********************************************')
        print('Level: Easy\n')
        print(
            'You have total 5 questions to be done in Easy level.\n'
            '----------------------------\nNumbers included = [0 - 5]\n'
            'Signs included = [+, -]\n----------------------------\n'
            'The time taken to complete the task will be shown')
        print("All the Best!")
        input('Press Enter to Start.')
        print('-------------------------')

        start_time = time.time()

        # Loop through total problems for the Easy level
        for i in range(TOTAL_PROBLEMS):
            exprmnt, answer = create_problem()
            while True:
                guess = input('Problem #' + str(i + 1) + ' : ' + exprmnt + ' = ')
                if guess == str(answer):
                    correct += 1
                    break
                else:
                    print('Wrong answer.')
                    wrong += 1
                    break

                i += 1

        finish_time = time.time()
        total_time = round(finish_time - start_time, 3)

        # Display results and grade for the Easy level
        print(f'You got {correct} correct answers and {wrong} wrong answers')
        gradee()

        print('You finished in: ', total_time, 'seconds')
        quit()

    if mode == 'h':
        def gradeh():
            # Evaluate and print the grade for the Hard level
            if correct > 11 or correct == 11:
                print('Excellent! You got A grade.')
            elif 7 < correct < 11:
                print("Good! You got B grade.")
            elif 3 < correct < 5:
                print("Need Improvement! You got C grade.")
            elif correct < 3 or correct == 3:
                print('Very Bad! You got D grade.')

        # Update constants for the Hard level
        SIGN = ['+', '-', '*']
        MIN_NUM = 1
        MAX_NUM = 30
        TOTAL_PROBLEMS = 15

        # Reset variables for the Hard level
        wrong = 0
        correct = 0

        # Introduction for the Hard level
        print('**********************************************')
        print('Level: Hard\n')
        print(
            'You have total 15 questions to be done in Hard level.\n'
            '----------------------------\nNumbers included = [1 - 30]\nSigns included = [+, -, *]\n'
            '----------------------------\nThe time taken to complete the task will be shown')
        print("All the Best!")
        input('Press Enter to Start.')
        print('-------------------------')

        start_time = time.time()

        # Loop through total problems for the Hard level
        for i in range(TOTAL_PROBLEMS):
            exprmnt, answer = create_problem()
            while True:
                guess = input('Problem #' + str(i + 1) + ' : ' + exprmnt + ' = ')
                if guess == str(answer):
                    correct += 1
                    break
                else:
                    print("Wrong answer.")
                    wrong += 1
                    break

                i += 1

        finish_time = time.time()
        total_time = round(finish_time - start_time, 3)

        # Display results and grade for the Hard level
        print(f'You got {correct} correct answers and {wrong} wrong answers')
        gradeh()

        print("You have finished in: ", total_time, 'seconds')
        quit()
