import tkinter
import pytube
import time
from mhmovie import Movie
from mhmovie import Music
import os

global url
Hdirect = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos')
path = Hdirect+'\\YTDL Videos'
Check = os.path.isdir(path)
audioPath = path+'\\audio'
vidPath = path+'\\vid'

print('Checking File structure')
if Check == False :
    print('Creating directorys')
    os.mkdir(path)
    os.mkdir(path+'\\vid')
    os.mkdir(path+'\\audio')
    pass
os.chdir(path)

def youtubeVidDL():
    if mp3State.get():
        videoToMp3()
        return
    print("Will commence Video download and proccessing now.")
    url = inputOne.get()
    if not url:
        return
    youtube = pytube.YouTube(url)
    video = youtube.streams
    video.get_audio_only().download(audioPath)
    Audtitle = video.get_audio_only().default_filename
    Audtitle2 = video.get_audio_only().title
    video = video.filter(adaptive=True).first()
    Vidtitle = video.default_filename
    video.download(vidPath)
    #post proccessing
    m = Movie(vidPath+'\\'+Vidtitle)
    mu = Music(audioPath+'\\'+Audtitle)

    final = m+mu
    final.save(path+'\\'+Vidtitle)
    print("Finished Rendering the video...Begining audio processing")
    VToMp3Post(Audtitle)
    return

def videoToMp3():
    print("Will download and convert audio file now.")
    url = inputOne.get()
    if not url:
        return
    youtube = pytube.YouTube(url)
    video = youtube.streams
    video.get_audio_only().download(audioPath)
    Audtitle = video.get_audio_only().default_filename
    Audtitle2 = video.get_audio_only().title
    #post proccessing
    VToMp3Post(Audtitle)
    return

def VToMp3Post(Audtitle):
    #Here we will process all audio clips to mp3 versions
    Audtitle2 = Audtitle
    if Audtitle2.endswith('.mp4'):
        Audtitle2 = Audtitle2[:-4]
        pass
    print('We have recieved the variables '+Audtitle+' and '+Audtitle2)
    mu = Movie(audioPath+'\\'+Audtitle)
    aud = mu.audio()
    aud.save(Audtitle2+".mp3")
    time.sleep(5)
    cmd1 = 'ren extract.mp3 "'+Audtitle2+'.mp3"'
    cwd = os.getcwd()
    if cwd != audioPath:
        os.chdir(audioPath)
        pass
    os.system('dir')
    os.system(cmd1)
    os.chdir(path)
    print("Finished all processes")
    return

def youtubeVidProDL():
    #under construction backup if the DASH download is unavailable.
    return

#def slugify(value):
#    import unicodedata
#    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
#    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
#    value = unicode(re.sub('[-\s]+', '-', value))
    # ...
#    return value

Main = tkinter.Tk(className="Youtube video Downloader")
Main.configure(bg="black")
icon = tkinter.PhotoImage(file = "C:/Users/craig/Documents/Python/YT DL/icon.png")
Main.iconphoto(False, icon)
mp3State = tkinter.IntVar()
Title = tkinter.Label(text="Please input the url for the video you would like to download.", bg="black", fg="white")
labelOne = tkinter.Label(text="URL:", bg="black", fg="white")
labelTwo = tkinter.Label(text="mp3", bg="black", fg="white")
inputOne = tkinter.Entry()
CheckBtn = tkinter.Checkbutton(bg="black", variable=mp3State)
DLButton = tkinter.Button(text="Download", bg="red", fg="white", command=youtubeVidDL)
Title.grid(row=0, column=0, columnspan=2)
labelOne.grid(row=1, column=0)
inputOne.grid(row=1, column=1)
CheckBtn.grid(row=2, column=1)
labelTwo.grid(row=2, column=0)
DLButton.grid(row=3, column=0, columnspan=2, pady=4)

Main.mainloop()
