import unittest
from phonebook import Phonebook

class TestPhonebook(unittest.TestCase):
    
    def setUp(self):
        self.cont = Phonebook()
        
    def test_if_add_method_adds_contact(self):
        result = self.cont.addContact("Jeff mutahi", 449)
        self.assertEqual(len(result), 1)
        
    def test_if_update_method_updates_contact(self):
        contact = self.cont.updateContact("Jeff Njogu", 949)
        self.assertEqual(contact, 949)
        
    def test_if_view_method_retreaves_contact(self):
        self.cont.updateContact("Jeff Njogu", 994)
        result = self.cont.contactList["Jeff Njogu"]
        self.assertEqual(result, 994)
        
    def test_if_delete_method_deletes_contact(self):
        self.cont.addContact("Jeff Njogu", 449)
        self.cont.delContact('Jeff Njogu')
        self.assertEqual(len(self.cont.contactList), 0)

    def test_delete_if_no_contact_saved(self):
        with self.assertRaises(KeyError):
            self.cont.delContact('John Doe')


if __name__ == "__main__":
    unittest.main()
