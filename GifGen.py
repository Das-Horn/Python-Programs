import sys
import os
import asyncio

def GenGif(Params):
    Path = ''

# Variables above

    print(os.getcwd())
    OutName = Params[2].split('\\')
    for i in range(len(OutName)-1):
        Path = Path +OutName[i] + "\\"
    print("\\")
    L = len(OutName)
    FileName = OutName[L-1]
#    FileName = FileName[:-4]
    os.chdir(Path)
    cmd = str('ffmpeg -ss '+Params[0]+' -t '+Params[1]+' -i "'+Params[2]+'" -vf "fps='+Params[3]+',scale='+Params[4]+':-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 "'+FileName[:-4]+'.gif"')
    os.system(cmd)
    return
 #REPLACE , With +
def GetInput():
    Params = ['','','','','','']
    Params[0] = input("Please enter the start time of the gif in the video. \n") #get start time
    Params[1] = input("Please enter a total length time for the video. \n") #get length

#    if Params[0] >= Params[1]:
#        print("The values you have entered are invalid please enter valid values.")
#        while Params[0] >= Params[1]:
#                Params[0] = input("Please enter the start time of the gif in the video.")
#                Params[1] = input("Please ente a total length time for the video.")
    Params[2] = input("please enter the full file path to the video input file \n")
    Params[3] = input("Please enter a framerate for the gif (default = 24) \n")
    Params[4] = input("Please enter a resolution for the gif (ex. 1080, 720, 480) \n")
    GenGif(Params)
    return

def main():
    print("Welcome to the python gif generator, This proram has a dependency on FFmpeg so please install this program first. :)")
    print("To stop the program please type 'STOP'")
    ENTRY = input("Please type 'Y' to continue \n")
    if ENTRY == 'Y':
        GetInput()
    return

main()
sys.exit(1)