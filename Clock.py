import tkinter as tk
from time import strftime

root=tk.Tk()
root.title("Digital Clock by Naveen Verma")

def time():
    t=strftime("%H:%M:%S %p \n %D")
    label.config(text=t)
    label.after(1000,time)

label=tk.Label(root, font=('calibri',50,'bold'),background='Black', foreground='White')
label.pack(anchor='center')

time()

root.mainloop()
