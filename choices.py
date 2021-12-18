import tkinter as tk
from tkinter.constants import RAISED, RIDGE, SUNKEN
from numpy import random

root=tk.Tk()
root.title("Choice Maker")
root.rowconfigure(1, minsize=600, weight=1)
root.columnconfigure(0, minsize=600, weight=1)

choi_frm = tk.Frame(root)
choi_frm.grid(row=0, column=0, sticky="ew")

choi_lbl = tk.Label(choi_frm, text="Enter Your Choices", relief=RIDGE, borderwidth=2)
choi_lbl.grid(row=0, column=0, sticky="ew")

choice_one=tk.Entry(choi_frm, width=30, relief=SUNKEN, borderwidth=4)
choice_one.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

choice_two=tk.Entry(choi_frm, width=30, relief=SUNKEN, borderwidth=4)
choice_two.grid(row=2, column=0, sticky="ew", padx=5)

choice_three=tk.Entry(choi_frm, width=30, relief=SUNKEN, borderwidth=4)
choice_three.grid(row=3, column=0, sticky="ew", padx=5)

answer=tk.Message(root, text="answers will appear here ", relief=SUNKEN, borderwidth=3)
answer.grid(row=1, column=0, sticky="nesw")

button = tk.Button(choi_frm, text="submit", relief=RAISED, borderwidth=3)

def pick(event):
    choices = []
    one = choice_one.get()
    choices.append(one)
    two=choice_two.get()
    choices.append(two)
    three=choice_three.get()
    choices.append(three)
    rn = random.randint(1,len(choices)+1)
    if rn == 1:
        answer=tk.Message(root, text=one, relief=SUNKEN, borderwidth=3)
        answer.grid(row=1, column=0, sticky="nesw")
    elif rn == 2:
        answer=tk.Message(root, text=two, relief=SUNKEN, borderwidth=3)
        answer.grid(row=1, column=0, sticky="nesw")
    elif rn == 3:
        answer=tk.Message(root, text=three, relief=SUNKEN, borderwidth=3)
        answer.grid(row=1, column=0, sticky="nesw")
    else:
        answer=tk.Message(root, text="THERE WAS AN ERROR PLEASE TRY AGAIN", relief=SUNKEN, borderwidth=3)
        answer.grid(row=1, column=0, sticky="nesw")

button.bind("<Button-1>", pick)
button.grid(row=5, column=0, sticky="ew", padx=5, pady=5)





root.mainloop()
