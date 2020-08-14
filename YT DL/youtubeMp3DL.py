import tkinter
import pytube
import time
from mhmovie.code import *

global url

def youtubeVidDL():
    url = inputOne.get()
    if not url:
        return
        pass
    youtube = pytube.YouTube(url)
    video = youtube.streams
    video.get_audio_only().download("vid/audio")
    Audtitle = video.get_audio_only().default_filename
    video = video.filter(adaptive=True).first()
    Vidtitle = video.default_filename
    video.download("vid/vid")
    #post proccessing
    m = movie("vid/vid/"+Vidtitle)
    mu = music('vid/audio/'+Audtitle)

    final = m+mu
    final.save("vid/"+Vidtitle)

    return

def videoToMp3():
    return

Main = tkinter.Tk(className="Youtube video Downloader")
Main.configure(bg="black")
Title = tkinter.Label(text="Please input the url for the video you would like to download.", bg="black", fg="white")
labelOne = tkinter.Label(text="URL:", bg="black", fg="white")
labelTwo = tkinter.Label(text="mp3", bg="black", fg="white")
inputOne = tkinter.Entry()
CheckBtn = tkinter.Checkbutton(bg="black")
DLButton = tkinter.Button(text="Download", bg="red", fg="white", command=youtubeVidDL)
Title.grid(row=0, column=0, columnspan=2)
labelOne.grid(row=1, column=0)
inputOne.grid(row=1, column=1)
CheckBtn.grid(row=2, column=1)
labelTwo.grid(row=2, column=0)
DLButton.grid(row=3, column=0, columnspan=2, pady=4)

Main.mainloop()
