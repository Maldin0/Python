'''PSCP Program'''
def main(guess, numbers):
    '''8427-Guess 06/11/2022'''
    while guess != 'END':
        guess = guess.split()
        if guess[2] == 'YES':
            if guess[0] == '=':
                numbers = [int(guess[1])]
            elif guess[0] == '<':
                numbers = [i for i in numbers if i < int(guess[1])]
            elif guess[0] == '>':
                numbers = [i for i in numbers if i > int(guess[1])]
        elif guess[2] == 'NO':
            if guess[0] == '=':
                numbers = [i for i in numbers if i != int(guess[1])]
            elif guess[0] == '<':
                numbers = [i for i in numbers if i >= int(guess[1])]
            elif guess[0] == '>':
                numbers = [i for i in numbers if i <= int(guess[1])]
        guess = input()
    print(*numbers)

main(input(), [int(i) for i in range(101)])
