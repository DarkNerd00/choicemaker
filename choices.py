import tkinter as tk
from random import randint

choices = []
r_num = random.randint(1,len(choices))


root = tk.Tk()
root.window("Choice Maker")
root.rowconfigure(0, minsize=600, weight=1)
root.columnconfigure(1, minsize=600, weight=1)

label = tk.frame()



root.mainloop()
