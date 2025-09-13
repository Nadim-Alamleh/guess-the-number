from random import randint 

rnum = randint(1,100)
name = input('Hello , what is your name :')
print(f'Well {name} I\'m thinking of a number between 1 and 100.\nTake a guess :')


num_of_guesses = 1

while num_of_guesses < 7:
    guess  = input()
    if guess.isdigit():
        if int(guess) >= 1 and int(guess) <= 100 :
            if int(guess) < rnum :
                print('TOO low')
            elif int(guess) > rnum :
                print('TOO high')
            elif int(guess) == rnum:
                break
            num_of_guesses+=1
        else:
            print('wrong input')
            break
    else:
        print('Please enter a valid number.')
if int(guess) == rnum :
    print(f'Good Job , you guess it in {num_of_guesses} guesses')
else :
    print(f'NO, the number was : {rnum}')


