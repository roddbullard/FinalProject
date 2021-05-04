"""
Program:        Handicap_main.py
Author:         Rodd Bullard
Purpose:        Instantiate and test the Handicapper class
"""
from Handicapper import Handicapper
from datetime import datetime

current_date = "{:%B %d, %Y}".format(datetime.now())
print(f"Current date is {current_date}")

h = Handicapper()
scores = h.get_scores()
print(f"There are {len(scores)} scores for golfer")
print(scores)
differentials = h.calculate_differentials(scores)
handicap_index = h.calculate_index(differentials)
print(f"Calculated handicap index is {handicap_index}")
