from tkinter import filedialog
from tkinter import *
import pygame
import os

root=Tk() #initializes program
root.title('Music player')  #root is the window
root.geometry("500x300")

pygame.mixer.init() #mixit allows to play audio

menubar=Menu(root)
root.config(menu=menubar)
songs=[]
current_song=""
paused=False
def load_music():
    global current_song
    root.directory=filedialog.askdirectory()
    
    for song in os.listdir(root.directory):
        name, ext=os.path.splitext(song)
        if ext =='.mp3':
            songs.append(song)
    
    for song in songs:
        songlist.insert("end", song)
        
    songlist.selection_set(0)
    current_song=songs[songlist.curselection()[0]]

organise_menu=Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Organise', menu=organise_menu)

def play_music():
    global current_song, paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused=False
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused=True
def next_music():
    global current_song, paused
    
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) +1)
        current_song=songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
        
    
def prev_music():
    global current_song, paused
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) -1)
        current_song=songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

songlist=Listbox(root, bg="green", fg="white", width=100, height=15)
songlist.pack() #adds to the root widget

play_image=PhotoImage(file='play.png')
pause_image=PhotoImage(file='pause.png')
next_image=PhotoImage(file='fast-forward.png')
prev_image=PhotoImage(file='previous.png')

control_frame=Frame(root)
control_frame.pack()
play_btn=Button(control_frame, image=play_image, borderwidth=0, command=play_music)
pause_btn=Button(control_frame, image=pause_image, borderwidth=0, command=pause_music)
next_btn=Button(control_frame, image=next_image, borderwidth=0, command=next_music)
prev_btn=Button(control_frame, image=prev_image, borderwidth=0, command=prev_music)


play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop() #runs up program - opens window

