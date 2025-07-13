import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app import create_app
from app.db import db, Student

class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def test_add_student(self):
        res = self.client.post('/api/v1/student', json={
            "name": "Alice", "age": 20, "email": "alice@example.com"
        })
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Alice", res.data)

    def test_get_students(self):
        self.client.post('/api/v1/student', json={
            "name": "Bob", "age": 22, "email": "bob@example.com"
        })
        res = self.client.get('/api/v1/student')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Bob", res.data)

if __name__ == "__main__":
    unittest.main()

