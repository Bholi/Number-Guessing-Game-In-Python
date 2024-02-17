from random import randint

attempts = 0
max_attempts = 3
while attempts < max_attempts:
    try:
        guessed_number = int(input('Guess any number between 1 to 10 : '))
        random_number = randint(1, 10)
        if guessed_number > random_number:
            print('The number is higher')
        elif guessed_number < random_number:
            print('The number is lower')
        else:
            print('Congratulations! you guessed the correct number')
            break
        attempts += 1

    except ValueError as e:
        print('Please enter valid number')
        continue
if attempts == max_attempts:
    print('Sorry, you have reached the maximum number of attempts.')
