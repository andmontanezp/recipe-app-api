from django.test import TestCase

from app.calc import add, substract


class CalcTests(TestCase):

    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)

    def test_substract_numbers(self):
        self.assertEqual(substract(5, 3), 2)
