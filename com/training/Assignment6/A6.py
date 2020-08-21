import abc
class Person:
    firstName = ""
    lastName = ""
    email = ""

    def __init__(self):
        pass

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, fName):
        self.firstName = fName

    def getLastName(self):
        return self.lastName

    def setLastName(self, lName):
        self.lastName = lName

    def toString(self):
        response = ""
        response = "Name: " + self.firstName + " " + self.lastName + "\n" + "Email: " + self.email
        return response

    abc.abstractmethod
    def getDisplayTest(self):
        pass


class Employee(Person):
    socialSecurity = ""

    def __init__(self):
        pass



    def getDisplayTest(self):
        response = ""
        response = "Name: " + self.firstName + " " + self.lastName + "\n" + "Email: " + self.email + "\n" + "Social security number" + self.socialSecurity
        return response

    def setSocialSecurity(self, socialSecurity):
        self.socialSecurity = socialSecurity

    def getSocialSecurity(self):
        return self.socialSecurity

class Customer(Person):
    customerNumber = ""

    def __init__(self):
        pass

    def getDisplayTest(self):
        response = ""
        response = "Name: " + self.firstName + " " + self.lastName + "\n" + "Email: " + self.email + "\n" + "Customer number" + self.customerNumber
        return response
    def setCustomerNumber(self, num):
        self.customerNumber = num

    def getCustomerNumber(self):
        return self.customerNumber

class Validator:

    def custOrEmp(self):
        response = input("Create customer or employee? (c/e): ")
        while (response != "c" and response != "e"):
            print("Error! This entry is required. Try again.")
            response = input("Create customer or employee? (c/e): ")

        return response

    def yesOrNo(self):
        response = input("Continue? (y/n): ")
        while (response != "y" and response != "n"):
            print("Error! This entry is required. Try again.")
            response = input("Continue? (y/n): ")

        return response

class PersonApp:
    def main(self):

        print("Welcome to the Person Tester application")
        valid = Validator()
        cont = "y"

        while(cont == "y"):
            userCustOrEmp = valid.custOrEmp()
            if(userCustOrEmp == "c"):
                userCust = Customer()
                firName = input("Enter first name: ")
                userCust.setFirstName(firName)
                lasName = input("Enter last name: ")
                userCust.setLastName(lasName)
                usEmail = input("Enter email address: ")
                userCust.setEmail(usEmail)
                custNum = input("Customer number: ")
                userCust.setCustomerNumber(custNum)

                print("You entered: ")
                print(userCust.getDisplayTest())
                cont = valid.yesOrNo()
            else:
                userEmp = Employee()
                firName = input("Enter first name: ")
                userEmp.setFirstName(firName)
                lasName = input("Enter last name: ")
                userEmp.setLastName(lasName)
                usEmail = input("Enter email address: ")
                userEmp.setEmail(usEmail)
                custNum = input("Social security number: ")
                userEmp.setSocialSecurity(custNum)

                print("You entered: ")
                print(userEmp.getDisplayTest())
                cont = valid.yesOrNo()


userPerson = PersonApp()
userPerson.main()





