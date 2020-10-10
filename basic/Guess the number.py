
import  random
def guessgame():
    """The function takes one input from the user . It asks
      the user to guess a number. With each turn ,the user is displayed the
      number of guesses used and the number of guesses left. If the user is
      unable to answer then, it gives a choice to the user to see the answer """
    x=random.randint(0,99)

    guess=9
    flag=0

    while(guess!=0):
        y=int(input("Enter your guess"))
        if (y == x):
            guess = guess - 1
            print("Congratulations!you've won")
            print("guesses used:", 9 - guess)
            print("guesses left:", 9 - (9 - guess))
            flag = 1
            break
        elif (y - x) > 3:
            guess = guess - 1
            print("Your guess is bigger")
            print("guesses used:", 9 - guess)
            print("guesses left:", 9 - (9 - guess))
        elif (y - x) < -3:
            guess = guess - 1;
            print("Your guess is smaller")
            print("guesses used:", 9 - guess)
            print("guesses left:", 9 - (9 - guess))
        elif (y - x) <= 3 and (y - x) >= 2:
            guess = guess - 1;
            print("Your guess is bigger but you are close")
            print("guesses used:", 9 - guess)
            print("guesses left:", 9 - (9 - guess))
        elif (y - x) >= -3 and (y - x) <= -2:
            guess = guess - 1
            print("Your guess is smaller but you are close")
            print("guesses used:", 9 - guess)
            print("guesses left:", 9 - (9 - guess))
        elif (y - x) == 1 or (y - x) == -1:
            guess = guess - 1
            print("you are very close")
            print("guesses used:", 9 - guess)
            print("guesses left:", 9 - (9 - guess))
    if (guess == 0 and flag != 1):
        print("GAME OVER!")
        y = input("Press y to know the answer else press n")
        if (y == 'y'):
            print(x, ".Don't say it to anyone else")
        else:
            print("Goodbye!")


