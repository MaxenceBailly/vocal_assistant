from tkinter import *
from tkinter import filedialog
import pygame

window = Tk()
window.title("Mp3 Player")
window.geometry("500x300")

pygame.mixer.init()

def add_song_command():
    song = filedialog.askopenfilename(initialdir="audio/", title="Choose the song", filetypes=(("mp3 Files", "*.mp3"), ))
    song = song.replace("C:/Users/maxen/Desktop/python_mp3/music/", "")
    song = song.replace(".mp3", "")
    song_box.insert(END, song)

def play():
    song = song_box.get(ACTIVE)
    song = (f"C:/Users/maxen/Desktop/python_mp3/music/{song}.mp3")
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

song_box = Listbox(window, bg="black", fg="green", width=100, selectbackground="red", selectforeground="black")
song_box.pack(pady=20)

frame = Frame(window)
frame.pack()

back = Button(frame)
forward = Button(frame)
play = Button(frame, command=play)
pause = Button(frame)
stop = Button(frame)

back.grid(row=0, column=0, padx=10)
forward.grid(row=0, column=1, padx=10)
play.grid(row=0, column=2, padx=10)
pause.grid(row=0, column=3, padx=10)
stop.grid(row=0, column=4, padx=10)

menu = Menu(window)
window.config(menu=menu)

add_song = Menu(menu)
menu.add_cascade(label="Add songs", menu=add_song)
add_song.add_command(label="add a song to the playlist", command=add_song_command)

window.mainloop()