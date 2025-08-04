from random import randint

secret_num = randint(1 , 20)
attempts = 0

def number_wrong(Cause , user_input):
    print(f"Number is {Cause} than {user_input}!")

while True:
    try:
        user_input = int(input('\nPlease select the number: '))
        attempts += 1
        if user_input <= 0 or user_input > 20:
            raise ValueError()
        if user_input > secret_num:
            number_wrong("less" , user_input)
        elif user_input < secret_num:
            number_wrong("bigger" , user_input)
        else:
            print(f"\nYOU WON! \n\nAttempts: {attempts}")
            break
    except ValueError:
        print('Please select a valid number(1 - 20!)')