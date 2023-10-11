"""
Customer Class
"""

import Person

class Customer(Person.Person):
    def __init__(self, name, address, phone, number, mail):
        Person.Person.__init__(self, name, address, phone)
        self.number = number
        self.mail = mail

    def setNumber(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def setMail(self, mail):
        self.mail = mail

    def getMail(self):
        return self.mail

    def mailList(self, mail):
        if mail == True:
            return "On the Mail List"
        else:
            return "Not on the Mail List"
    def __str__(self):
        return "\nName: {}\nAddress: {}\nPhone: {}\nMail:{}\nNumber: {}". format(self.getName(), self.getAddress(), self.getPhone(),self.mailList(self.getMail),self.getNumber())
    
        
