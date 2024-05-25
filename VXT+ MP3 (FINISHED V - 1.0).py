from pygame import mixer
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

print("VXT+ MP3 is a project by Sharavan Premathas")
print("Users of this (Downloadees 'per say') may alter this code")


root = Tk()
root.geometry("440x180")
img = ImageTk.PhotoImage(Image.open("VXT+ LOGO.png"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.after(2000,root.destroy)
root.mainloop()

mixer.init()

def Play():
    global current_song
    if current_song:
        mixer.music.load(current_song)
        mixer.music.play()
        song_label.config(text=f"Playing: {current_song.split('/')[-1]}")


def Pause():
    mixer.music.fadeout(1000)
    

def Pause2():
    mixer.music.pause()
    home.destroy()

def set_volume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)

def pick_song():
    global current_song
    current_song = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if current_song:
        song_label.config(text=f"Selected: {current_song.split('/')[-1]}")

home = Tk()
home.title("VXT+ MP3 Player")
home.geometry("510x200")
home.configure(bg="#333")
home.resizable(False, False)  

font = ("Helvetica", 12)

volume_slider = Scale(home, from_=0, to=100, orient=HORIZONTAL, command=set_volume, length=300, 
                      bg="#444", fg="white", troughcolor="#555", highlightthickness=0)
volume_slider.set(50)
volume_slider.pack(pady=10)

text = Label(home, text="VXT+ MP3", font=("Helvetica", 16), bg="#333", fg="white")
text.pack(pady=10)

controls_frame = Frame(home, bg="#333")
controls_frame.pack(pady=10)

button = Button(controls_frame, text="Play", command=Play, font=font, bg="#4CAF50", fg="white", 
                activebackground="#45a049", width=10)
button.grid(row=0, column=0, padx=5)

button2 = Button(controls_frame, text="Pause", command=Pause, font=font, bg="#f44336", fg="white", 
                 activebackground="#e53935", width=10)
button2.grid(row=0, column=1, padx=5)

button3 = Button(controls_frame, text="Pick Song", command=pick_song, font=font, bg="#008CBA", fg="white", 
                 activebackground="#007BB5", width=10)
button3.grid(row=0, column=2, padx=5)

button4 = Button(controls_frame, text="Quit", command=Pause2, font=font, bg="#555", fg="white", 
                 activebackground="#444", width=10)
button4.grid(row=0, column=3, padx=5)

song_label = Label(home, text="No song selected", font=font, bg="#333", fg="white")
song_label.pack(pady=10)

current_song = None


home.mainloop()