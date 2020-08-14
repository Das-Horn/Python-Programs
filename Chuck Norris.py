import tkinter
import http.client
import time
import json

global x
x = 1

def apiRequest():
    global x
    count = str(x) + '. '
    conn = http.client.HTTPSConnection("matchilling-chuck-norris-jokes-v1.p.rapidapi.com")
    headers = {
        'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com",
        'x-rapidapi-key': "ab7ac11b7amsh9c220aac72e3667p149b24jsnb38423a7ebd3",
        'accept': "application/json"
        }
    conn.request("GET", "/jokes/random", headers=headers)
    res = conn.getresponse()
    data = res.read().decode('utf-8')
    fin = json.loads(data)
    print(fin["value"])
    entry.insert('end', count)
    entry.insert('end', fin["value"])
    entry.insert('end', "\n \n")
    entry.see(tkinter.END)
    Main.update()
    x = x+1
    entry.after(5000, apiRequest)


Main = tkinter.Tk()
label = tkinter.Label(text="Here are some Chuck Norris jokes for your troubles. :)")
frame = tkinter.Frame(Main, width=1920, height=1080)
entry = tkinter.Text(frame, width=1920, height=1080)
frame.pack_propagate(0)
frame.pack()
label.pack()
entry.pack()

apiRequest()
Main.mainloop()
