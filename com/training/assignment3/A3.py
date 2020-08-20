class Circle:
    radius = 0.0
    totalCount = 0

    def __init__(self, rad):
        a = Validator()
        radius = rad

    def getCircumference(self):
        cir = 0.0
        import math
        cir = 2 * math.pi * radius
        Circle.totalCount += 1
        return cir

    def getFormattedCircumference(self):
        forCir = ""
        forCir = format(self.getCircumference(), '.2f')
        return forCir

    def getArea(self):
        area = 0.0
        import math
        area = math.pi * radius * radius
        return area

    def getFormattedArea(self):
        forArea = ""
        forArea = format(self.getArea(), '.2f')
        return forArea

    def formatNumber(x):
        forNum = ""
        forNum = format(x, '.2f')
        return forNum

    def getObjectCount(self):
        return self.totalCount


class Validator:

    def validNum(self):
        x = 2
        while (x < 5):
            user = input("Enter number:")
            try:
                val = int(user)
                if (val > 0):
                    x = 6
            except ValueError:
                print("Thats not a number! Try again!!")
        return val


    def validResponse(self):
        x = 0
        while (x < 1):
            answer = input("Try again? (y/n) : ")
            if (answer == "y" or answer == "n"):
                x = 1
        return answer


validRad = Validator()
response = "y"
while (response == "y"):
    radius = validRad.validNum()
    testCircle = Circle(radius)
    print("Circumference " + testCircle.getFormattedCircumference())
    print("Area: " + testCircle.getFormattedArea())
    response = validRad.validResponse()

print("Goodbye. You created ")
print(testCircle.getObjectCount())
print("circle(s)")
print("Bye - Come back soon!")







