"""
Program:        test_Handicapper.py
Author:         Rodd Bullard
Purpose:        Run unit tests against the Handicapper module
"""

import unittest

from Handicapper import Handicapper

class MyTestCase(unittest.TestCase):

    def test_get_scores(self):
        expected = [77, 80, 85, 100, 72, 79]
        actual  = Handicapper.get_scores(self)
        self.assertEqual(expected, actual)

    def test_calculate_differentials(self):
        expected = [8.66, 7.72, 9.61, 5.84]
        scores = [80, 79, 81, 77]
        actual  = Handicapper.calculate_differentials(self, scores)
        self.assertEqual(expected, actual)

    def test_calculate_index(self):
        expected = 6.8
        diffs = [8.66, 7.72, 9.61, 5.84]
        actual  = Handicapper.calculate_index(self, diffs)
        self.assertEqual(expected, actual)

