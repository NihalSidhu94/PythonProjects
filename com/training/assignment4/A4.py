class Die:
    value = 0
    sides = 0

    def __init__(self):
        self.sides = 6

    def __init__(self, sidesValue):
        self.sides = sidesValue

    def roll(self):
        import random
        self.value = random.randint(1, 6)

    def getValue(self):
        return self.value


class PairOfDice:
    die1 = Die(6)
    die2 = Die(6)
    sumOfDies = 0

    def __init__(self):
        die1 = Die(6)
        die2 = Die(6)

    def __init__(self, userSides):
        die1 = Die(userSides)
        die2 = Die(userSides)

    def roll(self):
        self.die1.roll()
        self.die2.roll()

    def getValue1(self):
        return self.die1.getValue()

    def getValue2(self):
        return self.die2.getValue()

    def getSum(self):
        sumOfDies = self.die1.getValue() + self.die2.getValue()
        return sumOfDies

class Validator:
    def validResponse(self):
        answer = ""
        x = 0
        answer = input("Roll again? (y/n)")
        if (answer == "y" or answer == "n"):
            x = 1
        while (x < 1):
            answer = input("Error! Entry must be 'y' or 'n'. Roll again?")
            if (answer == "y" or answer == "n"):
                x = 1
        return answer

    def validStartResponse(self):
        answer = ""
        x = 0
        answer = input("Roll the dice? (y/n)")
        if (answer == "y" or answer == "n"):
            x = 1
        while (x < 1):
            answer = input("Error! Entry must be 'y' or 'n'. Roll again?")
            if (answer == "y" or answer == "n"):
                x = 1
        return answer

print("Welcome to the Paradise Roller application")

response = ""
validDice = Validator()
response = validDice.validStartResponse()

if(response == "y"):
    while(response == "y"):
        ValidDie = Validator()
        newDice = PairOfDice(6)
        newDice.roll()

        firstValue = newDice.getValue1()
        secondValue = newDice.getValue2()
        print(firstValue)
        print(secondValue)

        sum = newDice.getSum()

        if(sum == 7):
            print("Craps!")
        elif(sum == 2):
            print("Snake eyes!")
        elif(sum == 12):
            print("Box cars!")
        response = ValidDie.validResponse()






