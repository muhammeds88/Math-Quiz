import random
import time

name = input('Enter your Name: ')

while True:
    def grade():
        if correct >= 8:
            print('Excellent! You got A grade.')
        elif correct > 5 and correct < 8:
            print("Good! You got B grade.")
        elif correct > 3 and correct < 5:
            print("Need Improvement! You got C grade.")
        elif correct <= 3:
            print('Very Bad! You got D grade.')


    SIGN = ['+', '-', '*']  # these are constants and cannot change
    MIN_NUM = 1
    MAX_NUM = 10
    TOTAL_PROBLEMS = 10


    def create_problem():
        left_num = random.randint(MIN_NUM, MAX_NUM)
        right_num = random.randint(MIN_NUM, MAX_NUM)
        operator = random.choice(SIGN)

        exprmnt = str(left_num) + ' ' + operator + ' ' + str(right_num)

        answer = eval(exprmnt)
        return exprmnt, answer


    wrong = 0
    correct = 0

    print('\nSample Test')

    print(f'Hello {name} welcome to Maths Test.\nYou have total 10 questions to be done in Sample Test.\n'
          f'----------------------------\nNumbers included = [1 - 10]\nSigns included = [+, -, *]\n'
          f'----------------------------\nThe time taken to complete the task will be shown')
    print("All the Best!")
    input('Press the Enter to Start.')
    print('-------------------------')

    start_time = time.time()

    for i in range(TOTAL_PROBLEMS):
        exprmnt, answer = create_problem()
        while True:
            guess = input('Problem #' + str(i + 1) + ' : ' + exprmnt + ' = ')
            if guess == str(answer):
                correct += 1
                break
            else:
                print("wrong answer.")
                wrong += 1
                break

            i += 1

    finish_time = time.time()
    total_time = round(finish_time - start_time, 3)  # round the numbers in to 3 digits

    print(f'You got {correct} correct answers and {wrong} wrong answers')
    grade()

    print("You have finished in: ", total_time, 'seconds')

    again = input("\nDo you wanna continue to the next level?(y or n) ")
    if again == 'y':
        print('Good\nSelect the level')
    else:
        quit()
    mode = input("Enter 'e' for Easy\nEnter 'h' for Hard\n")

    if mode == 'e':
        def gradee():
            if correct > 4:
                print('Excellent! You got A grade.')
            elif correct == 4:
                print("Good! You got B grade.")
            elif correct == 3:
                print("Need Improvement! You got C grade.")
            elif correct <= 2:
                print('Very Bad! You got D grade.')


        MIN_NUM = 0
        MAX_NUM = 5
        SIGN = ['+', '-']
        TOTAL_PROBLEMS = 5


        def create_problem():
            left_num = random.randint(MIN_NUM, MAX_NUM)
            right_num = random.randint(MIN_NUM, MAX_NUM)
            operator = random.choice(SIGN)

            exprmnt = str(left_num) + ' ' + operator + ' ' + str(right_num)

            answer = eval(exprmnt)
            return exprmnt, answer


        wrong = 0
        correct = 0

        print('**********************************************')
        print('Level: Easy\n')
        print(
            'You have total 5 questions to be done in Easy level.\n'
            '----------------------------\nNumbers included = [0 - 5]\n'
            'Signs included = [+, -]\n----------------------------\n'
            'The time taken to complete the task will be shown')
        print("All the Best!")
        input('Press the Enter to Start.')
        print('-------------------------')

        start_time = time.time()

        for i in range(TOTAL_PROBLEMS):
            exprmnt, answer = create_problem()
            while True:
                guess = input('Problem #' + str(i + 1) + ' : ' +  exprmnt + ' = ')
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

        print(f'You got {correct} correct answers and {wrong} wrong answers')
        gradee()

        print('You finished in: ', total_time, 'seconds')
        quit()

    if mode == 'h':
        def gradeh():
            if correct > 11 or correct == 11:
                print('Excellent! You got A grade.')
            elif correct > 7 and correct < 11:
                print("Good! You got B grade.")
            elif correct > 3 and correct < 5:
                print("Need Improvement! You got C grade.")
            elif correct < 3 or correct == 3:
                print('Very Bad! You got D grade.')


        SIGN = ['+', '-', '*']  # these are constants and cannot change
        MIN_NUM = 1
        MAX_NUM = 30
        TOTAL_PROBLEMS = 15


        def create_problem():
            left_num = random.randint(MIN_NUM, MAX_NUM)
            right_num = random.randint(MIN_NUM, MAX_NUM)
            operator = random.choice(SIGN)

            exprmnt = str(left_num) + ' ' + operator + ' ' + str(right_num)

            answer = eval(exprmnt)
            return exprmnt, answer
        wrong = 0
        correct = 0

        print('**********************************************')
        print('Level: Hard\n')
        print(
            'You have total 15 questions to be done in Hard level.\n'
            '----------------------------\nNumbers included = [1 - 30]\nSigns included = [+, -, *]\n'
            '----------------------------\nThe time taken to complete the task will be shown')
        print("All the Best!")
        input('Press the Enter to Start.')
        print('-------------------------')

        start_time = time.time()

        for i in range(TOTAL_PROBLEMS):
            exprmnt, answer = create_problem()
            while True:
                guess = input('Problem #' + str(i + 1) + ' : ' + exprmnt + ' = ')
                if guess == str(answer):
                    correct += 1
                    break
                else:
                    print("wrong answer.")
                    wrong += 1
                    break

                i += 1

        finish_time = time.time()
        total_time = round(finish_time - start_time, 3)  # round the numbers in to 3 digits

        print(f'You got {correct} correct answers and {wrong} wrong answers')
        gradeh()

        print("You have finished in: ", total_time, 'seconds')
        quit()