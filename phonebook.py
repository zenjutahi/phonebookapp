from unittest.mock import patch
import  unittest

class Contact:
    name = ""
    number = ""
 
def addContact():
    print()
    contact = Contact()
    contact.name = input("Enter contact name: ")
    contact.number = input("Enter contact number: ")
    contactList.append(contact)
    print("Contact added.")
    print()
     
def getMenuChoice():
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Quit")
    return input("Please enter your choice (1-3): ")
 
def viewContacts():
    print()
    print("Printing contacts...")
    for itm in contactList:
        print (itm.name + ", " + itm.number),
    print()
 
#Tests using the mock patch

class Test(unittest.TestCase):  
    @patch('__main__.addContact', return_value='Timothy')
    def test_answer_yes(self, input):
        self.assertEqual(addContact(), 'Timothy')

    @patch('__main__.addContact', return_value='3')
    def test_answer_no(self, input):
        self.assertIsNotNone(addContact())


if __name__ == '__main__':
    unittest.main()
    contactList = []
    choice = getMenuChoice()
    while choice != "3":
        if choice == "1":
            addContact()
        elif choice == "2":
            viewContacts()
        choice = getMenuChoice()
    print()
    print("Goodbye.")

    