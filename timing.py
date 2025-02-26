from tkinter import *
import pygame.midi as md
# from time import sleep

looping = False
bpm = 250

def main():
    global player
    global root

    backColor = '#303030'

    root = Tk()
    root.title("Test Timing")
    root.geometry('500x400')
    root.config(bg=backColor)

    mainFrame = Frame(root, bg=backColor)
    mainFrame.pack()

    md.init()
    player = md.Output(0)
    player.set_instrument(121, 0)

    btnStart = Button(mainFrame, text="Start", command=tglLoop)
    btn = Button(mainFrame, text="Click", command=clicked)
    btnStart.pack()
    btn.pack()

    root.mainloop()
    md.quit()

def tglLoop():
    global looping
    looping = not looping
    if looping:
        startLoop()

def startLoop():
    global looping
    global player
    global root
    global bpm
    global start

    if looping:
        start = md.time()
        player.note_on(60, 127, 0)
        root.after(bpm * 2, metOff)
        
def metOff():
    global player
    global stop
    stop = md.time()
    player.note_off(60,70,0)
    print(stop - start)
    startLoop()

def clicked():
    global player
    global clicking
    global bpm
    global root
    global start
    player.set_instrument(127, 0)
    player.note_on(60, 70, 0)
    player.set_instrument(121, 0)
    now = md.time() - start
    root.after(bpm, clickerOff)
    # print(f"             {now}")
    if now > bpm:
        now -= bpm
    now = bpm - now
    print(f"             {now}")
    root.after(now, pianoOn)
def clickerOff():
    global player
    player.note_off(60, 70, 0)

def pianoOn():
    global player
    global bpm
    global root
    player.set_instrument(0, 0)
    player.note_on(60, 100, 0)
    player.set_instrument(121, 0)
    root.after(bpm, pianoOff)
def pianoOff():
    global player
    player.note_off(60, 100, 0)





if __name__ == '__main__':
    main()