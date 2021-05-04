"""
Program:        Handicapp_GUI.py
Author:         Rodd Bullard
Purpose:        Display GUI for Handicapper application
"""

import tkinter as tk
from functools import partial
from Handicapper import Handicapper
import sqlite3
from sqlite3 import Error

def add_score(conn, score_entry):
    score = []
    score_str = score_entry.get()
    def convert_score():
        #score.append(50)
        score.append('4/21/2021')
        #score.append(score_str)
        try:
            score.append(int(score_str))
        except:
            print(f"Score needs to a numeric integer: {score_str}")
            raise ValueError
    try:
        convert_score()
    except:
        print(f"Score will not be added")
        return
    print(score)
    sql = ''' INSERT INTO scores(date_played, score)
          VALUES( ?, ?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, score)
        conn.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cur.rowcount)
        cur.close()
        print(f"Score of {score_str} has been added")
    except Error as err:
        print(err)



def enter_score():
    child = tk.Toplevel(main)
    child.geometry("400x100")
    child.title("Handicapper(v1.0) - Score Entry")
    score_var = ""
    score_label = tk.Label(child, text = 'Score', font=('calibre',10, 'bold'))
    score_entry = tk.Entry(child,textvariable = score_var, font=('calibre',10,'normal'))
    score_entry.focus_set()
    sub_btn=tk.Button(child,text = 'Submit', command = partial(add_score, conn, score_entry))
    can_btn=tk.Button(child,text = 'Quit', command = child.destroy)
    score_label.grid(row=0,column=0)
    score_entry.grid(row=0,column=1)
    sub_btn.grid(row=1,column=0)
    can_btn.grid(row=1,column=1)
    child.mainloop()


def calculate_index(scores):
    child = tk.Toplevel(main)
    child.geometry("400x100")
    child.title("Handicapper(v1.0) - Handicap Index")
    differentials = h.calculate_differentials(h.get_scores())
    handicap_index = h.calculate_index(differentials)
    handicap_string = "Current Handicap Index is " + str(handicap_index)
    label = tk.Label(child, text=handicap_string)
    label.grid(row=0)
    quit_button = tk.Button(child,
                   text="Quit",
                   #fg="black",
                   width=25,
                   command=child.destroy)
    quit_button.grid(row=1, column=1)
    child.mainloop()


if __name__ == '__main__':
    h = Handicapper()
    try:
        conn = sqlite3.connect("CIS189.db")
    except Error as err:
        print(err)
    scores = h.get_scores()
    main = tk.Tk()
    main.geometry("400x100")
    main.title("Handicapper(v1.0) - Main Menu")
    frame = tk.Frame(main)
    frame.pack()
    score_button = tk.Button(main,
                       text="Enter Score",
                       #fg="black",
                       width=25,
                       command=enter_score)
    score_button.pack()
    index_button = tk.Button(main,
                       text="Calculate Index",
                       #fg="black",
                       width=25,
                       command=partial(calculate_index, scores))
    index_button.pack()
    quit_button = tk.Button(main,
                       text="Quit",
                       #fg="black",
                       width=25,
                       command=main.destroy)
    quit_button.pack()
    main.mainloop()
