import os, sys
from pygame import *

def menu():
    print ("+-----------------------MENU----------------------+")
    print ("|    1    |     2     |   3    |   4    |   5     |")
    print ("+-------------------------------------------------+")
    print ("|  Pause  |  Unpause  |  Play  |  Stop  |  Load   |")
    print ("+-------------------------------------------------+")
    x = input("Enter Choice: ")
    return x.strip()

def list_songs(songs):
    for i, song in enumerate(songs):
        print(i+1, ". ", song)
    return int(input("Enter the song index which you want to play..."))

def action(songs,x):
    if x == '1':
        mixer.music.pause()
    if x == '2':
        mixer.music.unpause()
    if x == '3':
        mixer.music.play(-1)
    if x == '4':
        mixer.music.stop()
    if x == '5':
        mixer.music.load(songs[list_songs(songs)-1])
        mixer.music.play(-1)

def play_music(songs,choice):
    mixer.init()
    mixer.music.load(songs[choice])
    mixer.music.play(-1)
    while mixer.music.get_busy():
        x = menu()
        action(songs,x)
        print('Playing')

def check_baseDir():
    songs=[]
    if len(sys.argv)>1:
        baseDir = sys.argv[1]
    else:
        baseDir = None
    if baseDir:
        for items in os.listdir(os.chdir(baseDir)):
            if items.endswith('.mp3'):
                songs.append(items)            
    else:
        for items in os.listdir(os.getcwd()):
            if items.endswith('.mp3'):
                songs.append(items)
    songs.sort()
    return songs

def main():
    songs=check_baseDir()

    #Get the list of songs from the current directory

    print('Welcome to the Terminal Music Player...\n')
    print('Below are the list of songs in directory')

    #If there are any songs in the directory
    if len(songs)>=1:
        try:
            choice=list_songs(songs)
            assert choice>=1
        except AssertionError:
            print('Please select at least one song')
        else:
            play_music(songs,choice-1)
    else:
        print('Sorry! There are no mp3s detected in your directory')
        print('Try stating another directory when you call this application')

if __name__ == '__main__':
    main()