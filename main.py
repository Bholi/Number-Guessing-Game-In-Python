from random import randint
while True:
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

    except ValueError as e:
        print('Please enter valid number')
        continue

