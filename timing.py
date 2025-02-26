from tkinter import *
import pygame.midi as md
# from time import sleep

looping = False
bpm = 250
hitCount = 0

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
    tglLoop()

    btnStart = Button(mainFrame, text="Start", command=tglLoop)
    btn = Button(mainFrame, text="Click", command=clicked)
    root.bind('<Return>', clickedE)
    btnStart.pack()
    btn.pack()

    root.bind('<Escape>', lambda x: root.destroy())
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
    global hitCount

    player.set_instrument(127, 0)
    player.note_on(60, 70, 0)
    player.set_instrument(121, 0)
    now = md.time() - start
    hitCount += 1

    root.after(bpm, clickerOff)

    if now > bpm:
        now -= bpm
    now = bpm - now
    print(f"             {now}")
    if hitCount > 0:
        root.after(now, pianoLoop)
def clickerOff():
    global player
    player.note_off(60, 70, 0)
def clickedE(e):
    clicked()

def pianoLoop():
    global hitCount

    wait = 0
    while hitCount > 0:
        root.after(wait, lambda x=hitCount-1: pianoOn(x))
        wait += 50
        hitCount -= 1

def pianoOn(pitchOffset):
    global player
    global bpm
    global root

    player.set_instrument(0, 0)
    player.note_on(60+pitchOffset, 100, 0)
    player.set_instrument(121, 0)

    if pitchOffset > 0: root.after(50, lambda x=pitchOffset: pianoOff(x))
    else: root.after(bpm, lambda x=pitchOffset: pianoOff(x))
def pianoOff(pitchOffset):
    global player
    player.note_off(60+pitchOffset, 100, 0)



if __name__ == '__main__':
    main()