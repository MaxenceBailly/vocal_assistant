from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.title("")

window.attributes("-alpha", 0.1)

l = Label(window, text="Hello")
l.pack()

def slide(x):
    window.attributes("-alpha", my_slider.get())
    slide_l.config(text=str(round(my_slider.get(), 2)))

my_slider = ttk.Scale(window, from_=0.1, to=1.0, value=0.7, orient=HORIZONTAL, command=slide)
my_slider.pack(pady=20)

slide_l = Label(window, text='')
slide_l.pack(pady=10)

def new_window():
    new = Toplevel()
    new.attributes("-alpha", 0.5)

new_window = Button(window, text="New", command=new_window)
new_window.pack(pady=20)

window.mainloop()