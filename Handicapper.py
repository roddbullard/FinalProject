"""
Program:        Handicapper.py
Author:         Rodd Bullard
Purpose:        Calculate golf handicaps based on scores recorded
                by a golfer on a single golf course
                Each score will render a differential that uses the
                rating and slope constatnt values for the golf course.
                A handicap index is calculated by using half of the
                score differentials (rounded down) after they are sorted
                in ascending order.
"""
from datetime import datetime
import sqlite3
from sqlite3 import Error

class Handicapper():

    """
    Obtains scores and returns a list of them
    """
    def get_scores(self):
        try:
            conn = sqlite3.connect("CIS189.db")
        except Error as err:
            print(err)
        cur = conn.cursor()
        cur.execute("SELECT score FROM scores")
        all_scores = cur.fetchall()
        scores = []
        for s in all_scores:
            scores.append(s[0])
        #print(scores)
        return scores

    """
    Takes in a list of scores and returns a list of calculated differentials
    """
    def calculate_differentials(self, in_scores):
        #  Constants used in calculation of differentials
        RATING = 70.8
        SLOPE = 120
        scores = in_scores
        differentials = []
        for score in scores:
            differential = round((score - RATING) * 113 / SLOPE, 2)
            print(f"Score of {score} has a differential of {differential}")
            differentials.append(differential)
        print(differentials)
        return differentials

    """
    Takes in a list of differentials and returns a handicap index (rounded to one position)
    """
    def calculate_index(self, in_differentials):
        differentials = in_differentials
        number_of_scores = len(differentials)
        scores_used = number_of_scores // 2    #  Use Floor division to determine number of scores to use
        print(f"{scores_used} scores out of {number_of_scores} will be used in handicap index calculation")
        differentials.sort()
        diffs = 0
        diffs_total = 0
        for diff in differentials:
            diffs = diffs + 1
            if diffs <= scores_used:
                print(f"Differential used: {diff}")
                diffs_total = diffs_total + diff
        return round(diffs_total/scores_used, 1)

