class AddressBookEntry:
    name = ""
    emailAddress = ""
    phoneNumber = " "

    def __init__(self, nameInput, emailInput, phoneInput):
        self.name = nameInput
        self.emailAddress = emailInput
        self.phoneNumber = phoneInput

    def setName(self, nameInput):
        self.name = nameInput

    def getName(self):
        return self.name

    def setEmail(self, emailInput):
        self.emailAddress = emailInput

    def getEmail(self):
        return self.emailAddress

    def setPhone(self, phoneInput):
        self.phoneNumber = phoneInput

    def getPhone(self):
        return self.phoneNumber


class AddressBookIO:
    addressList = []
    a = "Bill Gates"
    b = "Bill@microsoft.com"
    c = "111-222-3333"
    Bill = AddressBookEntry(a, b, c)
    addressList.append(Bill)

    d = "Larry Ellison"
    e = "Larry@Oracle.com"
    f = "444-555-6666"
    Larry = AddressBookEntry(d, e, f)
    addressList.append(Larry)

    g = "Steve Jobs"
    h = "Steve@apple.com"
    i = "777-888-9999"
    Steve = AddressBookEntry(g, h, i)
    addressList.append(Steve)

    def getEntriesString(self):
        entries = ""
        currentEntry = ""
        x = 0
        currentName = ""
        currentEmail = ""
        currentPhone = ""

        while (x < len(self.addressList)):
            currentName = self.addressList[x].getName()
            currentName = format(currentName, '<25')
            currentEmail = self.addressList[x].getEmail()
            currentEmail = format(currentEmail, '<25')
            currentPhone = self.addressList[x].getPhone()
            currentPhone = format(currentPhone, '<25')
            currentEntry = currentName + " " + currentEmail + " " + currentPhone
            entries = entries + currentEntry
            entries = entries + "\n"
            x = x + 1
        return entries

    def saveEntry(self, n):
        self.addressList.append(n)


class Validator:

    def validNumber(self):
        val = 10
        x = 2
        while (x < 5):
            user = input("Enter number:")
            try:
                val = int(user)
                if (val > 0 and val < 4):
                    x = 6
            except ValueError:
                print("That's not a number! Try again!!")

        return val


class AddressBookEntryApp:
    choice = -1

    def display(self):
        print("1 - List entries")
        print("2 - add entry")
        print("3 - exit")
        Entries = AddressBookIO()
        validCheck = Validator()
        number = validCheck.validNumber()

        if (number == 1):
            print(Entries.getEntriesString())
            self.display()
        elif (number == 2):
            nameUser = input("Enter name: ")
            emailUser = input("Enter email address: ")
            phoneUser = input("Enter phone number: ")
            newUser = AddressBookEntry(nameUser, emailUser, phoneUser)
            Entries.saveEntry(newUser)
            self.display()
        elif (number == 3):
            print("Goodbye.")


c = AddressBookEntryApp()
c.display()


