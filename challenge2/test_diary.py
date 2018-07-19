from flask import *
import diary
from diary import *
import unittest
import json

class Test_Diary(unittest.TestCase):
    def setUp(self):
        self.app = diary.app.test_client()
   
    def test_register(self):
        app.testing=True
        response= self.app.get('/api/v1/register')
        self.assertEqual(response.status_code, 405)

    def test_view_users(self):
        app.testing=True
        response=self.app.get('/api/v1/all_users')
        self.assertEqual(response.status_code,200)
       
        

if __name__ =='__main__':
    unittest.main()

