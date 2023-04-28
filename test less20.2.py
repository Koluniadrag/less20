import unittest
import json
from unittest.mock import mock_open, patch
from phonebook import load_phonebook

class TestLoadPhonebook(unittest.TestCase):

    def test_load_phonebook(self):
        book_name = "test_book"
        phonebook = {"1234567890": {"name": "John", "surname": "Doe", "phone": "1234567890", "city": "New York"}}
        json_data = json.dumps(phonebook)

        with patch("builtins.open", mock_open(read_data=json_data)):
            result = load_phonebook(book_name)
        self.assertEqual(result, phonebook)
if __name__ == "__main__":
 unittest.main()



