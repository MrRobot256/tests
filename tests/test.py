import unittest
import app
import json
from io import StringIO
from unittest.mock import patch


class Test(unittest.TestCase):

    def setUp(self):
        with open('/Users/ivansviridov/Documents/Netology_py_dev/tests/fixtures/directories.json', 'r',
                  encoding='utf-8') as directories:
            app.directories = json.load(directories)
        with open('/Users/ivansviridov/Documents/Netology_py_dev/tests/fixtures/documents.json', 'r',
                  encoding='utf-8') as documents:
            app.documents = json.load(documents)

    def test_get_info(self):
        with patch('app.input', return_value='11-2'):
            self.assertEqual('Геннадий Покемонов', app.get_doc_owner_name())

    def test_print_all(self):
        with patch('sys.stdout', new=StringIO()) as my_out:
            app.show_all_docs_info()
            self.assertEqual(my_out.getvalue().strip(), 'Список всех документов:\n\npassport "2207 876234" "Василий '
                                                        'Гупкин"\ninvoice "11-2" "Геннадий Покемонов"\ninsurance '
                                                        '"10006" "Аристарх Павлов"')

    def test_adding(self):
        with patch('app.input', return_value='123'):
            app.add_new_shelf()
        self.assertIn('123', app.directories)

    def test_deleting(self):
        self.assertIn('11-2', app.directories['1'])
        app.remove_doc_from_shelf('11-2')
        self.assertNotIn('11-2', app.directories['1'])
