import pytube
import time
from mhmovie.code import *

print("Give URL:")
url = input()
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
