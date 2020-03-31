from tkinter import *
import tkinter.messagebox
from pygame import mixer


root = Tk()

# Creating a Menu Bar
menubar = Menu(root)
root.config(menu=menubar)


def about_us():
    tkinter.messagebox.showwarning(
        'About Melody', 'This is a Music Player using python')


# Creating Sub-Menu Bar
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New File")
subMenu.add_command(label="Open")
subMenu.add_command(label="Exit", command=root.destroy)

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="Contact Us")
subMenu.add_command(label="About Us", command=about_us)

mixer.init()  # Initialising the Mixer

root.geometry('300x300')
root.title = ("Melody")
root.iconbitmap(r'music.ico')

text = Label(root, text="Let's Get Started")
text.pack()

# Labelphoto = Label(root, image=playPhoto)
# Labelphoto.pack()


def play_music():
    mixer.music.load("song.mp3")
    mixer.music.play()
    print("Hey It Works")


def stop_music():
    mixer.music.stop()


def set_volume(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)
    # Set volume of mixer & it takes value between 0 to 1.


playPhoto = PhotoImage(file='play.png')
play_Btn = Button(root,  image=playPhoto, command=play_music)
play_Btn.pack()


stopPhoto = PhotoImage(file='stop.png')
stop_Btn = Button(root,  image=stopPhoto, command=stop_music)
stop_Btn.pack()


scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(5)
scale.pack()

root.mainloop()
