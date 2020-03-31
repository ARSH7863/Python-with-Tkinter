import tkinter as tk
from tkinter import *
import webbrowser


win = tk.Tk()  # main variables
win.title('Web Browser')  # GUI title
win.geometry("400x400")  # Width & Height of the GUI box
win.iconbitmap(r'globe.ico')  # Icon for the GUI box

# Search function to search any link


def search():
    url = entry.get()
    webbrowser.open(url)

# Google function to get redirected to it


def google():
    webbrowser.open('https://www.google.com')

# Youtube function to get redirected to it


def youtube():
    webbrowser.open('https://www.youtube.com')

# Amazon function to get redirected to it


def amazon():
    webbrowser.open('https://www.amazon.com')

# Facebook function to get redirected to it


def facebook():
    webbrowser.open('https://www.facebook.com')


igoogle = PhotoImage(file="google.png")
google = tk.Button(win, image=igoogle, command=google)

google.grid(row=1, column=0)


iyoutube = PhotoImage(file="youtube.png")
youtube = tk.Button(win, image=iyoutube, command=youtube)
youtube.grid(row=1, column=1)


iamazon = PhotoImage(file="amazon.png")
amazon = tk.Button(win, image=iamazon, command=amazon)
amazon.grid(row=0, column=0)


ifacebook = PhotoImage(file="facebook.png")
facebook = tk.Button(win, image=ifacebook, command=facebook)
facebook.grid(row=0, column=1)

label1 = Label(win, text='Enter URL Here : ', font=('arial', 12, 'bold'))
label1.grid(row=3, column=0)

entry = Entry(win, width=30)
entry.grid(row=4, column=1)

button = Button(win, text="Search", command=search)
button.grid(row=5, column=0, columnspan=2, pady=10)

win.mainloop()
