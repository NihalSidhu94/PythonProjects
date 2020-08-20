class OOValidator:

    def __init__(self):
        pass

    def getInt(self, prompt):
        x = 0
        while (x < 5):
            user = input(prompt)
            try:
                val = int(user)
            except ValueError:
                print("Error! Invalid integer value. Try again")

        return val

    def getIntWithinRange(self, prompt, min, max):
        x = 0
        while (x < 5):
            user = input(prompt)
            try:
                val = int(user)
                if (val >= min and val <= max):
                    x = 6
            except ValueError:
                print("Error! Invalid integer value. Try again")

        return val

    def getDouble(self, prompt):
        x = 0
        while (x < 5):
            user = input(prompt)
            try:
                val = float(user)
            except ValueError:
                print("Error! Invalid double value. Try again")

        return val

    def getDoubleWithinRange(self, prompt, min, max):
        x = 0
        while (x < 5):
            user = input(prompt)
            try:
                val = float(user)
                if (val >= min and val <= max):
                    x = 6
            except ValueError:
                print("Error! Invalid double value. Try again")

        return val

class MyValidator(OOValidator):

    def getRequiredString(self, prompt):
        response = input(prompt)
        return response

    def getChoiceString(self,prompt, s1, s2):

        response = input(prompt)
        while(response != s1 and response != s2):
            print("Error! This entry is required. Try again.")
            response = input(prompt)

        return response

class ValidatorTestApp:

    def main(self):
        print("Welcome to the Validation Tester application")
        valid = MyValidator()
        intPrompt = "Enter an integer between -100 and 100: "
        doublePrompt = "Enter any number between -100 and 100: "
        stringTest = "Enter your email address: "
        choiceTest = "Select one (x/y):";

        print("Int Test")
        minimum = 0
        maximum = 100
        valid.getIntWithinRange(intPrompt, minimum, maximum)
        print()
        print("Double Test")
        valid.getDoubleWithinRange(doublePrompt, 0, 100)
        print()
        print("Required String Test")
        valid.getRequiredString(stringTest)
        print()
        print("Required Choice Test")
        valid.getChoiceString(choiceTest, "x", "y");



test = ValidatorTestApp()
test.main()





