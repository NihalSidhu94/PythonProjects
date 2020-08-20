class GuesserNum:
    totalGuesses = 0

    randNum = 0
    currentGuess = 0

    def start(self):
        print("I'm thinking of a number from 1 to 100.")
        print("Try to guess it")

    def validNumber(self):
        x = 2
        while (x < 5):
            user = input("Enter number:")
            try:
                val = int(user)
                if (val > 0 and val < 101):
                    x = 6
            except ValueError:
                print("Thats not a number! Try again!!")

        return val

    def range(self):
        import random
        randNum = random.randint(1, 101)
        totalGuesses = 0
        currentGuess = self.validNumber()

        while (currentGuess != randNum):
            difference = currentGuess - randNum
            if (difference > 10):
                print("Way too high!")
                currentGuess = self.validNumber()
                totalGuesses = totalGuesses + 1
            if (difference < 10 and difference > 0):
                print("Too High!")
                currentGuess = self.validNumber()
                totalGuesses = totalGuesses + 1
            if (difference < 0):
                print("Too Low")
                currentGuess = self.validNumber()
                totalGuesses = totalGuesses + 1
            if (currentGuess == randNum):
                print('You got it in', totalGuesses, 'tries.')
                if (totalGuesses < 3):
                    print("Great work! You are a mathematical wizard")
                elif (totalGuesses > 3 and totalGuesses <= 7):
                    print("Not too bad, you've got some potential.")
                else:
                    print("What took you so long? Maybe you should take some lessons.")
        self.restart()

    def restart(self):
        x = 0
        while (x < 1):
            answer = input("Try again? (y/n) : ")
            if (answer == "y" or answer == "n"):
                x = 1
        if (answer == "y"):
            personA = GuesserNum()
            personA.start()
            personA.range()
        elif (answer == "n"):
            print("Bye - Come back soon!")


person = GuesserNum()
person.start()
person.range()

