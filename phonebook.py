class Phonebook:

    def __init__(self):

        self.contactList = {}
    
    def addContact(self, nameVr, numVr):
        "Method to add contact"
        self.contactList[nameVr] = numVr
        return self.contactList
    
    def updateContact(self, nameVr, numVr):
        "Method to update contact"
        self.contactList[nameVr] = numVr
        return self.contactList[nameVr]
        
    
    def delContact(self, nameVr):
        "Method to delete contact"
        if nameVr in self.contactList:
            del self.contactList[nameVr]
        else:
            raise KeyError
    
        