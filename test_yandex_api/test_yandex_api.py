import unittest
import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


class Test(unittest.TestCase):
    def test_server_response(self):
        params = dict(key=API_KEY, text='hello', lang='en' + '-{}'.format('ru'))
        response = requests.get(URL, params=params).json()
        self.assertEqual(408, response['code'])

    def test_positive_answer(self):
        params = dict(key=API_KEY, text='hi', lang='en' + '-{}'.format('ru'))
        response = requests.get(URL, params=params).json()
        self.assertEqual('привет', response['text'])

    def test_negative_answer(self):
        params = dict(key=API_KEY, text='netology', lang='en' + '-{}'.format('ru'))
        response = requests.get(URL, params=params).json()
        self.assertNotEqual('привет', response['code'])

    def test_wrong_key(self):
        params = dict(key='IT_IS_A_WROG_KEY', text='hello', lang='en' + '-{}'.format('ru'))
        response = requests.get(URL, params=params).json()
        self.assertNotEqual(408, response['code'])