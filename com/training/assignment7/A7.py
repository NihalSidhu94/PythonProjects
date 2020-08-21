class Countable:
    def incrementCount(self):
        pass
    def resetCount(self):
        pass
    def getCount(self):
        pass
    def getCountString(self):
        pass

class Alligator(Countable):
    count = 1

    def incrementCount(self):
        self.count = self.count+1

    def resetcount(self):
        self.count = 1

    def getCount(self):
        return self.count

    def getCountString(self):
        countReturn = ""
        countReturn = str(self.count) + " alligator"
        return countReturn

class Sheep(Countable):

    count = 1
    name = ""

    def incrementCount(self):
        self.count = self.count +1

    def resetCount(self):
        self.count = 1

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getCount(self):
        return self.count

    def getCountString(self):
        countReturn = ""
        countReturn = str(self.count) + " " + str(self.name)
        return countReturn

    def clone(self):
        cloneSheep = Sheep()
        cloneSheep.setName(self.name)
        return cloneSheep


class CountUtil:
    def count(self, Countable, maxCount):
        while(Countable.getCount() <= maxCount):
            print(Countable.getCountString())
            Countable.incrementCount()

class CountTestApp:

    def main(self):
        animalAll = Alligator()
        animalCounter = CountUtil()
        print("Counting alligators... \n")
        animalCounter.count(animalAll, 3)
        print()

        print("Counting sheep... \n")
        animalShe = Sheep()
        animalShe.setName("Blackie")
        animalCounter.count(animalShe, 2)
        print()

        animalDol = animalShe.clone()
        animalDol.resetCount()
        animalDol.setName("Dolly")
        animalCounter.count(animalDol, 3)
        print()

        animalShe.resetCount()
        animalCounter.count(animalShe, 1)


test = CountTestApp()
test.main()




