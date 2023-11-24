import pygame
from tkinter import Scale
from customtkinter import CTk,CTkButton,CTkEntry,CTkLabel,CTkSlider
from pygame import mixer
from tkinter.filedialog import askopenfile
mixer.init()
pygame.init()

        #    Creating Windows
window=CTk()
window.geometry('400x400+100')
window.resizable(False,False)

       #Global Numerals
global user_file 
# creating Functions for all
def Load_music():
    user_file=askopenfile()
    mixer.music.load(user_file.name)
    app_label.configure(text= user_file.name.split('/')[-1])

# app_label.config(text=user_file.name.split("/")[-1])

def pause_music():
    mixer.music.pause()

def play_music():
    mixer.music.play()


def rewind_music():
    mixer.music.rewind()

def stop_music():
    mixer.music.stop()

def volume_responsiveness(value):
    mixer.music.set_volume(value)


 # creating widget and displaying the widget and wired the command from the functions 

app_label=CTkLabel(window,text="")
app_label.place(x=180,y=50)



app_pause=CTkButton(window,text='Pause',command=pause_music)
app_pause.place(x=20,y=90)

app_play=CTkButton(window,text='Play',command=play_music)
app_play.place(x=230,y=90)

app_rewind=CTkButton(window,text='Rewind',command=rewind_music)
app_rewind.place(x=120,y=150)

app_load=CTkButton(window,text='Load',command=Load_music)
app_load.place(x=20,y=250)

app_stop=CTkButton(window,text="Stop",command=stop_music)
app_stop.place(x=230,y=250)


app_volume=CTkSlider(window,from_=0,to=1,command=volume_responsiveness)
app_volume.place(x=50, y=350)


window.mainloop()